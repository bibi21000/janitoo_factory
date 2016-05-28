# -*- coding: utf-8 -*-

"""Unittests for Janitoo-common.
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
import time
import unittest
import threading
import logging
from pkg_resources import iter_entry_points
import mock
import ConfigParser
from ConfigParser import RawConfigParser

sys.path.insert(0,os.path.dirname(__name__))

from janitoo_nosetests import JNTTBase
from janitoo_nosetests.values import JNTTFactory, JNTTFactoryCommon, JNTTFactoryPollCommon, JNTTFactoryConfigCommon

from janitoo.runner import Runner, jnt_parse_args
from janitoo.server import JNTServer
from janitoo.options import JNTOptions

from janitoo_factory.buses.fsm import JNTFsmBus

class TestRreadValue(JNTTFactory, JNTTFactoryConfigCommon, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='rread_value'

class TestRwriteValue(JNTTFactory, JNTTFactoryConfigCommon):
    """Test the value factory
    """
    entry_name='rwrite_value'

class TestActionString(JNTTFactory, JNTTFactoryCommon):
    """Test the value factory
    """
    entry_name='action_string'

class TestActionBoolean(JNTTFactory, JNTTFactoryCommon):
    """Test the value factory
    """
    entry_name='action_boolean'

class TestActionInteger(JNTTFactory, JNTTFactoryCommon):
    """Test the value factory
    """
    entry_name='action_integer'

class TestActionSwitchBinary(JNTTFactory, JNTTFactoryCommon):
    """Test the value factory
    """
    entry_name='action_switch_binary'

class TestActionSwitchMultilevel(JNTTFactory, JNTTFactoryCommon):
    """Test the value factory
    """
    entry_name='action_switch_multilevel'

class TestListString(JNTTFactory, JNTTFactoryCommon):
    """Test the value factory
    """
    entry_name='action_list'

class TestActionFsm(JNTTFactory, JNTTFactoryConfigCommon, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='transition_fsm'
    bus = JNTFsmBus(oid='test_bus')

    def get_main_value(self, node_uuid='test_node', **kwargs):
        return JNTTFactory.get_main_value(
                    self,
                    node_uuid = node_uuid,
                    fsm_bus = self.bus,
                    **kwargs)

    def test_100_value_entry_config(self):
        bus = JNTFsmBus(oid='test_bus')
        node_uuid='test_node'
        main_value = self.get_main_value(node_uuid=node_uuid)
        print main_value
        config_value = main_value.create_config_value()
        print config_value
        main_value.set_config(node_uuid, 0, 'working')
        self.assertEqual('working', main_value.get_config(node_uuid, 0))
        #~ self.assertTrue(main_value.ping_ip(node_uuid, 0))
        main_value.set_config(node_uuid, 0, 'sleeping')
        self.assertEqual('sleeping', main_value.get_config(node_uuid, 0))
        #~ self.assertFalse(main_value.ping_ip(node_uuid, 0))
