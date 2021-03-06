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

from janitoo.value_factory import JNTValueFactoryEntry

##############################################################
#Check that we are in sync with the official command classes
#Must be implemented for non-regression
from janitoo.classes import COMMAND_DESC

COMMAND_CONFIGURATION = 0x0070
COMMAND_SENSOR_BINARY = 0x0030
COMMAND_SENSOR_MULTILEVEL = 0x0031
COMMAND_NETWORK_CONTROLLER = 0x1051

assert(COMMAND_DESC[COMMAND_NETWORK_CONTROLLER] == 'COMMAND_NETWORK_CONTROLLER')
assert(COMMAND_DESC[COMMAND_CONFIGURATION] == 'COMMAND_CONFIGURATION')
assert(COMMAND_DESC[COMMAND_SENSOR_BINARY] == 'COMMAND_SENSOR_BINARY')
assert(COMMAND_DESC[COMMAND_SENSOR_MULTILEVEL] == 'COMMAND_SENSOR_MULTILEVEL')
##############################################################

def make_sensor_integer(**kwargs):
    return JNTValueSensorInteger(**kwargs)

def make_sensor_byte(**kwargs):
    return JNTValueSensorByte(**kwargs)

def make_sensor_float(**kwargs):
    return JNTValueSensorFloat(**kwargs)

def make_network_controller(**kwargs):
    return JNTValueNetworkController(**kwargs)

class JNTValueSensorGeneric(JNTValueFactoryEntry):
    """
    """
    def __init__(self, **kwargs):
        """
        """
        genre = kwargs.pop('genre', 0x01)
        is_readonly = kwargs.pop('is_readonly', True)
        is_writeonly = kwargs.pop('is_writeonly', False)
        index = kwargs.pop('index', 0)
        JNTValueFactoryEntry.__init__(self,
            index=index, genre=genre,
            is_readonly=is_readonly, is_writeonly=is_writeonly,
            **kwargs)

    def create_poll_value(self, **kwargs):
        """
        """
        default = kwargs.pop('default', 30)
        return self._create_poll_value(default=default, **kwargs)

class JNTValueNetworkController(JNTValueFactoryEntry):
    def __init__(self, entry_name="network_controller", **kwargs):
        """
        """
        genre = kwargs.pop('genre', 0x04)
        hhelp = kwargs.pop('help', 'Primary/secondary network controller')
        label = kwargs.pop('label', 'Network controller')
        cmd_class = kwargs.pop('cmd_class', COMMAND_NETWORK_CONTROLLER)
        list_tiems = kwargs.pop('list_tiems', ['primary', 'secondary'])
        JNTValueFactoryEntry.__init__(self,
            entry_name=entry_name,
            genre=genre,
            help=hhelp,
            label=label,
            list_tiems=list_tiems,
            cmd_class=cmd_class,
            type=0x05,
            **kwargs)

class JNTValueSensorFloat(JNTValueSensorGeneric):
    def __init__(self, entry_name="sensor_float", **kwargs):
        """
        """
        hhelp = kwargs.pop('help', 'A float sensor')
        label = kwargs.pop('label', 'Float')
        cmd_class = kwargs.pop('cmd_class', COMMAND_SENSOR_MULTILEVEL)
        JNTValueSensorGeneric.__init__(self, entry_name=entry_name, help=hhelp, label=label,
            cmd_class=cmd_class, type=0x03, **kwargs)

class JNTValueSensorByte(JNTValueSensorGeneric):
    def __init__(self, entry_name="sensor_byte", **kwargs):
        """
        """
        hhelp = kwargs.pop('help', 'A byte sensor')
        label = kwargs.pop('label', 'Byte')
        cmd_class = kwargs.pop('cmd_class', COMMAND_SENSOR_MULTILEVEL)
        JNTValueSensorGeneric.__init__(self, entry_name=entry_name, help=hhelp, label=label,
            cmd_class=cmd_class, type=0x02, **kwargs)

class JNTValueSensorInteger(JNTValueSensorGeneric):
    def __init__(self, entry_name="sensor_integer", **kwargs):
        """
        """
        hhelp = kwargs.pop('help', 'An integer sensor')
        label = kwargs.pop('label', 'Integer')
        cmd_class = kwargs.pop('cmd_class', COMMAND_SENSOR_MULTILEVEL)
        JNTValueSensorGeneric.__init__(self, entry_name=entry_name, help=hhelp, label=label,
            cmd_class=cmd_class, type=0x04, **kwargs)

