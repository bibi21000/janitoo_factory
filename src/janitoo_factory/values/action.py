# -*- coding: utf-8 -*-
"""The value

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
logger = logging.getLogger(__name__)

from janitoo.classes import VALUE_DESC
from janitoo.value_factory import JNTValueFactoryEntry

##############################################################
#Check that we are in sync with the official command classes
#Must be implemented for non-regression
from janitoo.classes import COMMAND_DESC

COMMAND_CONFIGURATION = 0x0070
COMMAND_SENSOR_BINARY = 0x0030
COMMAND_SENSOR_MULTILEVEL = 0x0031
COMMAND_SWITCH_BINARY = 0x0025
COMMAND_SWITCH_MULTILEVEL = 0x0026
COMMAND_BUTTON_BINARY = 0x3000
COMMAND_BUTTON_MULTILEVEL = 0x3001
COMMAND_FSM = 0x10B0
COMMAND_SHUTTER_BINARY = 0x3150
COMMAND_SHUTTER_MULTILEVEL = 0x3151

assert(COMMAND_DESC[COMMAND_SHUTTER_BINARY] == 'COMMAND_SHUTTER_BINARY')
assert(COMMAND_DESC[COMMAND_SHUTTER_MULTILEVEL] == 'COMMAND_SHUTTER_MULTILEVEL')
assert(COMMAND_DESC[COMMAND_FSM] == 'COMMAND_FSM')
assert(COMMAND_DESC[COMMAND_CONFIGURATION] == 'COMMAND_CONFIGURATION')
assert(COMMAND_DESC[COMMAND_SENSOR_BINARY] == 'COMMAND_SENSOR_BINARY')
assert(COMMAND_DESC[COMMAND_SENSOR_MULTILEVEL] == 'COMMAND_SENSOR_MULTILEVEL')
assert(COMMAND_DESC[COMMAND_SWITCH_BINARY] == 'COMMAND_SWITCH_BINARY')
assert(COMMAND_DESC[COMMAND_SWITCH_MULTILEVEL] == 'COMMAND_SWITCH_MULTILEVEL')
assert(COMMAND_DESC[COMMAND_BUTTON_BINARY] == 'COMMAND_BUTTON_BINARY')
assert(COMMAND_DESC[COMMAND_BUTTON_MULTILEVEL] == 'COMMAND_BUTTON_MULTILEVEL')
##############################################################

def make_action_string(**kwargs):
    return JNTValueActionString(**kwargs)

def make_action_byte(**kwargs):
    return JNTValueActionByte(**kwargs)

def make_action_integer(**kwargs):
    return JNTValueActionInteger(**kwargs)

def make_action_boolean(**kwargs):
    return JNTValueActionBoolean(**kwargs)

def make_action_list(**kwargs):
    return JNTValueActionList(**kwargs)

def make_action_switch_binary(**kwargs):
    return JNTValueActionSwitchBinary(**kwargs)

def make_action_switch_multilevel(**kwargs):
    return JNTValueActionSwitchMultilevel(**kwargs)

def make_action_shutter_binary(**kwargs):
    return JNTValueActionShutterBinary(**kwargs)

def make_action_shutter_multilevel(**kwargs):
    return JNTValueActionShutterMultilevel(**kwargs)

def make_action_button_binary(**kwargs):
    return JNTValueActionButtonBinary(**kwargs)

def make_action_button_multilevel(**kwargs):
    return JNTValueActionButtonMultilevel(**kwargs)

def make_transition_fsm(**kwargs):
    return JNTValueTransitionFsm(**kwargs)

class JNTValueActionGeneric(JNTValueFactoryEntry):
    def __init__(self, **kwargs):
        """
        """
        genre = kwargs.pop('genre', 0x02)
        is_readonly = kwargs.pop('is_readonly', False)
        is_writeonly = kwargs.pop('is_writeonly', False)
        index = kwargs.pop('index', 0)
        JNTValueFactoryEntry.__init__(self,
            index=index,
            genre=genre,
            is_readonly=is_readonly,
            is_writeonly=is_writeonly,
            **kwargs)

class JNTValueActionString(JNTValueActionGeneric):
    def __init__(self, entry_name="action_string", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A string')
        label = kwargs.pop('label', 'String')
        JNTValueActionGeneric.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            type=0x08,
            **kwargs)

class JNTValueActionByte(JNTValueActionGeneric):
    def __init__(self, entry_name="action_byte", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A byte')
        label = kwargs.pop('label', 'Byte')
        JNTValueActionGeneric.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            type=0x02,
            **kwargs)

class JNTValueActionInteger(JNTValueActionGeneric):
    def __init__(self, entry_name="action_integer", **kwargs):
        """
        """
        help = kwargs.pop('help', 'An integer')
        label = kwargs.pop('label', 'Integer')
        JNTValueActionGeneric.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            type=0x04,
            **kwargs)

class JNTValueActionBoolean(JNTValueActionGeneric):
    def __init__(self, entry_name="action_boolean", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A boolean')
        label = kwargs.pop('label', 'Boolean')
        JNTValueActionGeneric.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            type=0x04,
            **kwargs)

class JNTValueActionList(JNTValueActionGeneric):
    def __init__(self, entry_name="action_list", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A string')
        label = kwargs.pop('label', 'String')
        JNTValueActionGeneric.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            type=0x05,
            **kwargs)

class JNTValueActionSwitchBinary(JNTValueActionList):
    def __init__(self, entry_name="action_switch_binary", **kwargs):
        """
        """
        label = kwargs.pop('label', 'Switch')
        list_items = kwargs.pop('list_items', ['on', 'off'])
        help = kwargs.pop('help', 'A switch. Valid values are : %s'%list_items)
        default = kwargs.pop('default', 0)
        JNTValueActionList.__init__(self,
            entry_name=entry_name,
            help=help,
            default=default,
            label=label,
            list_items=list_items,
            cmd_class=COMMAND_SWITCH_BINARY,
            **kwargs)

class JNTValueActionSwitchMultilevel(JNTValueActionByte):
    def __init__(self, entry_name="action_switch_multilevel", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A dimmer. A byte from 0 to 100')
        label = kwargs.pop('label', 'dimmer')
        default = kwargs.pop('default', 0)
        min = kwargs.pop('min', 0)
        max = kwargs.pop('max', 0)
        JNTValueActionByte.__init__(self,
            entry_name=entry_name,
            help=help,
            default=default,
            label=label,
            min=min,
            max=max,
            cmd_class=COMMAND_SWITCH_MULTILEVEL,
            **kwargs)

class JNTValueActionShutterBinary(JNTValueActionList):
    def __init__(self, entry_name="action_shutter_binary", **kwargs):
        """
        """
        label = kwargs.pop('label', 'Shutter')
        list_items = kwargs.pop('list_items', ['up', 'down', 'stop'])
        help = kwargs.pop('help', 'A shutter. Valid values are : %s'%list_items)
        default = kwargs.pop('default', 0)
        JNTValueActionList.__init__(self,
            entry_name=entry_name,
            help=help,
            default=default,
            label=label,
            list_items=list_items,
            cmd_class=COMMAND_SHUTTER_BINARY,
            **kwargs)

class JNTValueActionShutterMultilevel(JNTValueActionByte):
    def __init__(self, entry_name="action_shutter_multilevel", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A shutter multilevel. A byte from 0 to 100')
        label = kwargs.pop('label', 'Shutterr')
        default = kwargs.pop('default', 0)
        min = kwargs.pop('min', 0)
        max = kwargs.pop('max', 0)
        JNTValueActionByte.__init__(self,
            entry_name=entry_name,
            help=help,
            default=default,
            label=label,
            min=min,
            max=max,
            cmd_class=COMMAND_SHUTTER_MULTILEVEL,
            **kwargs)

class JNTValueActionButtonBinary(JNTValueActionList):
    def __init__(self, entry_name="action_button_binary", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A button')
        label = kwargs.pop('label', 'Button')
        list_items = kwargs.pop('list_items', ['on', 'off'])
        default = kwargs.pop('default', 'off')
        JNTValueActionList.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            default=default,
            list_items=list_items,
            cmd_class=COMMAND_BUTTON_BINARY,
            **kwargs)

class JNTValueActionButtonMultilevel(JNTValueActionByte):
    def __init__(self, entry_name="action_button_mutlilevel", **kwargs):
        """
        """
        help = kwargs.pop('help', 'A button')
        label = kwargs.pop('label', 'Button')
        default = kwargs.pop('default', 'off')
        JNTValueActionByte.__init__(self,
            entry_name=entry_name,
            help=help,
            label=label,
            default=default,
            cmd_class=COMMAND_BUTTON_MULTILEVEL,
            **kwargs)

class JNTValueTransitionFsm(JNTValueActionList):

    def __init__(self, entry_name="transition_fsm", fsm_bus=None, **kwargs):
        """Manage a fsm on a bus
        """
        self._fsm_bus = fsm_bus
        if self._fsm_bus is None:
            raise RuntimeError("You must define fsm_bus parameter")
        help = kwargs.pop('help', 'Trigger a transition on the fsm or get the last triggered')
        label = kwargs.pop('label', 'Transit')
        genre = kwargs.pop('genre', 0x01)
        list_items = kwargs.pop('list_items', ['sleep','work'])
        get_data_cb = kwargs.pop('get_data_cb', self.get_transition)
        set_data_cb = kwargs.pop('set_data_cb', self.set_transition)
        JNTValueActionList.__init__(self,
            entry_name=entry_name, genre=genre,
            get_data_cb=get_data_cb, set_data_cb=set_data_cb,
            list_items=list_items,
            cmd_class=COMMAND_FSM,
            help=help,
            label=label,
            **kwargs)

    def __del__(self):
        """
        """
        self._fsm_bus = None

    def create_config_value(self, **kwargs):
        """
        """
        help = kwargs.pop('help', 'The initial transition to apply (at boot)')
        default = kwargs.pop('default', 'sleep')
        return self._create_config_value(type=0x08, help=help, default=default)

    def create_poll_value(self, **kwargs):
        """
        """
        default = kwargs.pop('default', 60)
        return self._create_poll_value(default=default, **kwargs)

    def get_transition(self, node_uuid, index):
        """Get the last transition applied to the machine
        """
        return self._data

    def set_transition(self, node_uuid, index, data):
        """Apply a transition
        """
        try:
            bus_cb = getattr(self._fsm_bus, data)
            bus_cb()
            self._data = data
        except Exception:
            logger.exception("[%s] - Error in set_transition %s", self.__class__.__name__, data)
