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
import logging
import threading
import mock
import logging

from janitoo_nosetests import JNTTBase
from janitoo_nosetests.server import JNTTDockerServerCommon, JNTTDockerServer

from janitoo.runner import Runner, jnt_parse_args
from janitoo.server import JNTServer
from janitoo.utils import HADD_SEP, HADD

import test_bus

class TestHTTPBus(test_bus.TestHTTPBus):
    def setUp(self):
        test_bus.TestHTTPBus.onlyDockerTest()
        test_bus.TestHTTPBus.setUp(self)

class TestRemoteBus(test_bus.TestRemoteBus):
    def setUp(self):
        test_bus.TestRemoteBus.onlyDockerTest()
        test_bus.TestRemoteBus.setUp(self)

class TestFsmBus(test_bus.TestFsmBus):
    def setUp(self):
        test_bus.TestFsmBus.onlyDockerTest()
        test_bus.TestFsmBus.setUp(self)

import test_values

class TestRreadValue(test_values.TestRreadValue):
    def setUp(self):
        test_values.TestRreadValue.onlyDockerTest()
        test_values.TestRreadValue.setUp(self)

class TestRwriteValue(test_values.TestRwriteValue):
    def setUp(self):
        test_values.TestRwriteValue.onlyDockerTest()
        test_values.TestRwriteValue.setUp(self)

class TestActionString(test_values.TestActionString):
    def setUp(self):
        test_values.TestActionString.onlyDockerTest()
        test_values.TestActionString.setUp(self)

class TestActionBoolean(test_values.TestActionBoolean):
    def setUp(self):
        test_values.TestActionBoolean.onlyDockerTest()
        test_values.TestActionBoolean.setUp(self)

class TestActionInteger(test_values.TestActionInteger):
    def setUp(self):
        test_values.TestActionInteger.onlyDockerTest()
        test_values.TestActionInteger.setUp(self)

class TestActionSwitchBinary(test_values.TestActionSwitchBinary):
    def setUp(self):
        test_values.TestActionSwitchBinary.onlyDockerTest()
        test_values.TestActionSwitchBinary.setUp(self)

class TestActionSwitchMultilevel(test_values.TestActionSwitchMultilevel):
    def setUp(self):
        test_values.TestActionSwitchMultilevel.onlyDockerTest()
        test_values.TestActionSwitchMultilevel.setUp(self)

class TestActionShutterBinary(test_values.TestActionShutterBinary):
    def setUp(self):
        test_values.TestActionShutterBinary.onlyDockerTest()
        test_values.TestActionShutterBinary.setUp(self)

class TestActionShutterMultilevel(test_values.TestActionShutterMultilevel):
    def setUp(self):
        test_values.TestActionShutterMultilevel.onlyDockerTest()
        test_values.TestActionShutterMultilevel.setUp(self)

class TestActionButtonBinary(test_values.TestActionButtonBinary):
    def setUp(self):
        test_values.TestActionButtonBinary.onlyDockerTest()
        test_values.TestActionButtonBinary.setUp(self)

class TestActionButtonMultilevel(test_values.TestActionButtonMultilevel):
    def setUp(self):
        test_values.TestActionButtonMultilevel.onlyDockerTest()
        test_values.TestActionButtonMultilevel.setUp(self)

class TestListString(test_values.TestListString):
    def setUp(self):
        test_values.TestListString.onlyDockerTest()
        test_values.TestListString.setUp(self)

class TestActionFsm(test_values.TestActionFsm):
    def setUp(self):
        test_values.TestActionFsm.onlyDockerTest()
        test_values.TestActionFsm.setUp(self)

import test_values_basic

class TestSensorFloat(test_values_basic.TestSensorFloat):
    def setUp(self):
        test_values_basic.TestSensorFloat.onlyDockerTest()
        test_values_basic.TestSensorFloat.setUp(self)

class TestSensorByte(test_values_basic.TestSensorByte):
    def setUp(self):
        test_values_basic.TestSensorByte.onlyDockerTest()
        test_values_basic.TestSensorByte.setUp(self)

class TestSensorInteger(test_values_basic.TestSensorInteger):
    def setUp(self):
        test_values_basic.TestSensorInteger.onlyDockerTest()
        test_values_basic.TestSensorInteger.setUp(self)

import test_values_config

class TestConfigString(test_values_config.TestConfigString):
    def setUp(self):
        test_values_config.TestConfigString.onlyDockerTest()
        test_values_config.TestConfigString.setUp(self)

class TestConfigPassword(test_values_config.TestConfigPassword):
    def setUp(self):
        test_values_config.TestConfigPassword.onlyDockerTest()
        test_values_config.TestConfigPassword.setUp(self)

class TestConfigInteger(test_values_config.TestConfigInteger):
    def setUp(self):
        test_values_config.TestConfigInteger.onlyDockerTest()
        test_values_config.TestConfigInteger.setUp(self)

class TestConfigByte(test_values_config.TestConfigByte):
    def setUp(self):
        test_values_config.TestConfigByte.onlyDockerTest()
        test_values_config.TestConfigByte.setUp(self)

class TestConfigList(test_values_config.TestConfigList):
    def setUp(self):
        test_values_config.TestConfigList.onlyDockerTest()
        test_values_config.TestConfigList.setUp(self)

class TestConfigArray(test_values_config.TestConfigArray):
    def setUp(self):
        test_values_config.TestConfigArray.onlyDockerTest()
        test_values_config.TestConfigArray.setUp(self)

class TestConfigBoolean(test_values_config.TestConfigBoolean):
    def setUp(self):
        test_values_config.TestConfigBoolean.onlyDockerTest()
        test_values_config.TestConfigBoolean.setUp(self)

class TestConfigFloat(test_values_config.TestConfigFloat):
    def setUp(self):
        test_values_config.TestConfigFloat.onlyDockerTest()
        test_values_config.TestConfigFloat.setUp(self)

import test_values_sensors

class TestSensorTemperature(test_values_sensors.TestSensorTemperature):
    def setUp(self):
        test_values_sensors.TestSensorTemperature.onlyDockerTest()
        test_values_sensors.TestSensorTemperature.setUp(self)

class TestSensorAltitude(test_values_sensors.TestSensorAltitude):
    def setUp(self):
        test_values_sensors.TestSensorAltitude.onlyDockerTest()
        test_values_sensors.TestSensorAltitude.setUp(self)

class TestSensorVoltage(test_values_sensors.TestSensorVoltage):
    def setUp(self):
        test_values_sensors.TestSensorVoltage.onlyDockerTest()
        test_values_sensors.TestSensorVoltage.setUp(self)

class TestSensorCurrent(test_values_sensors.TestSensorCurrent):
    def setUp(self):
        test_values_sensors.TestSensorCurrent.onlyDockerTest()
        test_values_sensors.TestSensorCurrent.setUp(self)

class TestSensorPercent(test_values_sensors.TestSensorPercent):
    def setUp(self):
        test_values_sensors.TestSensorPercent.onlyDockerTest()
        test_values_sensors.TestSensorPercent.setUp(self)

class TestSensorFrequency(test_values_sensors.TestSensorFrequency):
    def setUp(self):
        test_values_sensors.TestSensorFrequency.onlyDockerTest()
        test_values_sensors.TestSensorFrequency.setUp(self)

class TestSensorHumidity(test_values_sensors.TestSensorHumidity):
    def setUp(self):
        test_values_sensors.TestSensorHumidity.onlyDockerTest()
        test_values_sensors.TestSensorHumidity.setUp(self)

class TestSensorPressure(test_values_sensors.TestSensorPressure):
    def setUp(self):
        test_values_sensors.TestSensorPressure.onlyDockerTest()
        test_values_sensors.TestSensorPressure.setUp(self)

class TestSensorDistance(test_values_sensors.TestSensorDistance):
    def setUp(self):
        test_values_sensors.TestSensorDistance.onlyDockerTest()
        test_values_sensors.TestSensorDistance.setUp(self)

class TestSensorRotationSpeed(test_values_sensors.TestSensorRotationSpeed):
    def setUp(self):
        test_values_sensors.TestSensorRotationSpeed.onlyDockerTest()
        test_values_sensors.TestSensorRotationSpeed.setUp(self)

class TestSensorString(test_values_sensors.TestSensorString):
    def setUp(self):
        test_values_sensors.TestSensorString.onlyDockerTest()
        test_values_sensors.TestSensorString.setUp(self)

class TestSensorFloat(test_values_sensors.TestSensorFloat):
    def setUp(self):
        test_values_sensors.TestSensorFloat.onlyDockerTest()
        test_values_sensors.TestSensorFloat.setUp(self)

class TestSensorList(test_values_sensors.TestSensorList):
    def setUp(self):
        test_values_sensors.TestSensorList.onlyDockerTest()
        test_values_sensors.TestSensorList.setUp(self)

class TestSensorByte(test_values_sensors.TestSensorByte):
    def setUp(self):
        test_values_sensors.TestSensorByte.onlyDockerTest()
        test_values_sensors.TestSensorByte.setUp(self)

class TestSensorInteger(test_values_sensors.TestSensorInteger):
    def setUp(self):
        test_values_sensors.TestSensorInteger.onlyDockerTest()
        test_values_sensors.TestSensorInteger.setUp(self)

class TestSensorMemory(test_values_sensors.TestSensorMemory):
    def setUp(self):
        test_values_sensors.TestSensorMemory.onlyDockerTest()
        test_values_sensors.TestSensorMemory.setUp(self)

class TestSensorOrientation(test_values_sensors.TestSensorOrientation):
    def setUp(self):
        test_values_sensors.TestSensorOrientation.onlyDockerTest()
        test_values_sensors.TestSensorOrientation.setUp(self)

class TestSensorPresence(test_values_sensors.TestSensorPresence):
    def setUp(self):
        test_values_sensors.TestSensorPresence.onlyDockerTest()
        test_values_sensors.TestSensorPresence.setUp(self)

class TestSensorRainTotal(test_values_sensors.TestSensorRainTotal):
    def setUp(self):
        test_values_sensors.TestSensorRainTotal.onlyDockerTest()
        test_values_sensors.TestSensorRainTotal.setUp(self)

class TestSensorRainRate(test_values_sensors.TestSensorRainRate):
    def setUp(self):
        test_values_sensors.TestSensorRainRate.onlyDockerTest()
        test_values_sensors.TestSensorRainRate.setUp(self)

class TestSensorWindDirection(test_values_sensors.TestSensorWindDirection):
    def setUp(self):
        test_values_sensors.TestSensorWindDirection.onlyDockerTest()
        test_values_sensors.TestSensorWindDirection.setUp(self)

class TestSensorWindAverage(test_values_sensors.TestSensorWindAverage):
    def setUp(self):
        test_values_sensors.TestSensorWindAverage.onlyDockerTest()
        test_values_sensors.TestSensorWindAverage.setUp(self)

class TestSensorWindGust(test_values_sensors.TestSensorWindGust):
    def setUp(self):
        test_values_sensors.TestSensorWindGust.onlyDockerTest()
        test_values_sensors.TestSensorWindGust.setUp(self)

class TestHttpSerser(JNTTDockerServer, JNTTDockerServerCommon):
    """Test the server
    """
    path = '/tmp/janitoo_test'
    broker_user = 'toto'
    broker_password = 'toto'
    server_class = JNTServer
    server_conf = "tests/data/test_server_http.conf"
    hadds = [HADD%(1118,0), HADD%(1118,1)]

class TestRemoteSerser(JNTTDockerServer, JNTTDockerServerCommon):
    """Test the server
    """
    loglevel = logging.DEBUG
    path = '/tmp/janitoo_test'
    broker_user = 'toto'
    broker_password = 'toto'
    server_class = JNTServer
    server_conf = "tests/data/test_server_remote.conf"
    hadds = [HADD%(1120,0), HADD%(1120,1), HADD%(1120,2), HADD%(1120,3), HADD%(1120,4)]
