# -*- coding: utf-8 -*-
"""The fsm bus
"""

__license__ = """
    This file is part of Janitoo.

    Janitoo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Janitoo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Janitoo. If not, see <http://www.gnu.org/licenses/>.

"""
__author__ = 'Sébastien GALLET aka bibi21000'
__email__ = 'bibi21000@gmail.com'
__copyright__ = "Copyright © 2013-2014-2015-2016 Sébastien GALLET aka bibi21000"

import logging
#~ logging.getLogger(__name__).addHandler(logging.NullHandler())
logger = logging.getLogger(__name__)

from pkg_resources import iter_entry_points

from janitoo.bus import JNTBus
from janitoo.fsm import HierarchicalMachine as Machine

class JNTFsmBus(JNTBus):
    """A bus managed with a fsm
    """
    states = [
       'booting',
       'sleeping',
       'working',
    ]
    """The fsm states :
    """

    transitions = [
        { 'trigger': 'work',
            'source': '*',
            'dest': 'working',
        },
        { 'trigger': 'sleep',
            'source': '*',
            'dest': 'sleeping',
        },
    ]
    """The fsm transitions
    """

    def __init__(self, **kwargs):
        """
        """
        JNTBus.__init__(self, **kwargs)
        self._fsm =  None
        """The finish state machine"""
        self._fsm_boot_timer = None
        """The timer that's start the finish state machine"""
        self._fsm_timer_delay = 3
        """The timer delay between 2 retries"""
        self._fsm_max_retries = 3
        """The max retries to boot the fsm"""
        self._fsm_retry = 0
        """The current retry to boot the fsm"""
        self.state = "booting"
        """Initial state of the fsm"""
        uuid="{:s}_transition".format(self.oid)
        self.values[uuid] = self.value_factory['transition_fsm'](options=self.options, uuid=uuid,
            node_uuid=self.uuid,
            list_items=[ v['trigger'] for v in self.transitions ],
            fsm_bus=self,
        )
        poll_value = self.values[uuid].create_poll_value()
        self.values[poll_value.uuid] = poll_value
        config_value = self.values[uuid].create_config_value()
        self.values[config_value.uuid] = config_value

        uuid="{:s}_state".format(self.oid)
        self.values[uuid] = self.value_factory['sensor_string'](options=self.options, uuid=uuid,
            node_uuid=self.uuid,
            help='The state of the fsm.',
            label='State',
        )
        poll_value = self.values[uuid].create_poll_value(default=60)
        self.values[poll_value.uuid] = poll_value

    def start(self, mqttc, trigger_thread_reload_cb=None):
        """Start the bus
        """
        self._fsm = self.create_fsm()
        JNTBus.start(self, mqttc, trigger_thread_reload_cb)

    def create_fsm(self):
        """Create the fsm
        """
        return Machine(self,
            states=self.states,
            transitions=self.transitions,
            title='Bus',
            initial='booting')

    def stop(self):
        """Stop the bus
        """
        self.stop_boot_timer()
        if self.state != 'booting':
            self.sleep()
        self._fsm = None
        JNTBus.stop(self)

    def check_heartbeat(self):
        """Check that the fsm is started

        """
        return self.state != 'booting'

    def stop_boot_timer(self):
        """Stop the boot timer

        """
        if self._fsm_boot_timer is not None:
            self._fsm_boot_timer.cancel()
            self._fsm_boot_timer = None

    def on_boot_timer(self):
        """Make a check using a timer.

        """
        try:
            self.stop_boot_timer()
            if self.state == 'booting':
                if self._fsm_retry > self._fsm_max_retries:
                    logger.errot("[%s] - Fail to boot fsm after %s retries", self.__class__.__name__, self._fsm_retry)
                else:
                    self._fsm_retry += 1
                    self._fsm_boot_timer = threading.Timer(self._fsm_timer_delay + self._fsm_retry*self.nodeman.slow_start)
                    self._fsm_boot_timer.start()
                    state = self.nodeman.find_bus_value('state_config').data

            else:
                logger.info("[%s] - fsm has booted in state %s", self.__class__.__name__, self.state)
        except :
            logger.exception("Error wheb trying to boot fsm at try %s", self._fsm_retry)
