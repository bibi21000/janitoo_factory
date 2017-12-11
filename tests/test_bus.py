# -*- coding: utf-8 -*-

"""Unittests for Janitoo-Roomba Server.
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

import warnings
warnings.filterwarnings("ignore")

import sys, os
import time, datetime
import unittest
import threading
import logging
from pkg_resources import iter_entry_points
import mock

from janitoo_nosetests.server import JNTTServer, JNTTServerCommon
from janitoo_nosetests.bus import JNTTBus, JNTTBusCommon
from janitoo_nosetests.component import JNTTComponent, JNTTComponentCommon

from janitoo.utils import json_dumps, json_loads
from janitoo.utils import HADD_SEP, HADD
from janitoo.utils import TOPIC_HEARTBEAT
from janitoo.utils import TOPIC_NODES, TOPIC_NODES_REPLY, TOPIC_NODES_REQUEST
from janitoo.utils import TOPIC_BROADCAST_REPLY, TOPIC_BROADCAST_REQUEST
from janitoo.utils import TOPIC_VALUES_USER, TOPIC_VALUES_CONFIG, TOPIC_VALUES_SYSTEM, TOPIC_VALUES_BASIC
from janitoo.runner import jnt_parse_args
from janitoo.options import JNTOptions

from janitoo_factory.threads.http import HttpBus
from janitoo_factory.threads.remote import RemoteBus
from janitoo_factory.buses.fsm import JNTFsmBus

class TestHTTPBus(JNTTBus, JNTTBusCommon):
    """Test the Bus
    """
    oid = 'http'
    bus = HttpBus

class TestRemoteBus(JNTTBus, JNTTBusCommon):
    """Test the Bus
    """
    oid = 'remote'
    bus = RemoteBus

class TestFsmBus(JNTTBus, JNTTBusCommon):
    """Test the Bus
    """
    oid = 'generic'
    bus = JNTFsmBus

    class FakeNodeman(object):
        slow_start = 0.1

        def __init__(self, bus, **kwargs):
            self.bus = bus

        def find_bus_value(self, value):
            print(self.bus.values["generic_%s"%value].to_dict())
            return self.bus.values["generic_%s"%value]

    def test_100_bus_fsm_boot(self):
        with mock.patch('sys.argv', ['test', 'start', '--conf_file=%s'%'tests/data/test_bus_fsm.conf']):
            options = vars(jnt_parse_args())
        jnt_options = JNTOptions(options)

        bus = self.bus(options=jnt_options)
        bus.nodeman = TestFsmBus.FakeNodeman(bus)
        bus._fsm_timer_delay = 2
        self.assertNotEqual(bus, None)
        bus.start(None)
        i = 0
        self.assertFalse(bus.check_heartbeat())
        while i<30 and bus.state == 'booting':
            time.sleep(0.5)
            i += 1
            print(bus.state)
        self.assertEqual('sleeping', bus.state)
        bus.work()
        time.sleep(0.25)
        self.assertEqual('working', bus.state)
        self.assertTrue(bus.check_heartbeat())
        bus.stop()
        time.sleep(0.25)
        self.assertEqual('sleeping', bus.state)
        self.assertTrue(bus.check_heartbeat())
