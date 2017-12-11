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

from .test_bus import TestHTTPBus, TestRemoteBus, TestFsmBus

class TestHTTPBusD(TestHTTPBus):
    def setUp(self):
        TestHTTPBus.onlyDockerTest()
        TestHTTPBus.setUp(self)

class TestRemoteBusD(TestRemoteBus):
    def setUp(self):
        TestRemoteBus.onlyDockerTest()
        TestRemoteBus.setUp(self)

class TestFsmBusD(TestFsmBus):
    def setUp(self):
        TestFsmBus.onlyDockerTest()
        TestFsmBus.setUp(self)

from .test_values import TestRreadValue, TestRwriteValue

class TestRreadValueD(TestRreadValue):
    def setUp(self):
        TestRreadValue.onlyDockerTest()
        TestRreadValue.setUp(self)

class TestRwriteValueD(TestRwriteValue):
    def setUp(self):
        TestRwriteValue.onlyDockerTest()
        TestRwriteValue.setUp(self)

from .test_values import TestActionString, TestActionBoolean, TestActionInteger, TestActionSwitchBinary
from .test_values import TestActionSwitchBinary, TestActionSwitchMultilevel
from .test_values import TestActionShutterBinary, TestActionShutterMultilevel
from .test_values import TestActionButtonBinary, TestActionButtonMultilevel

class TestActionStringD(TestActionString):
    def setUp(self):
        TestActionString.onlyDockerTest()
        TestActionString.setUp(self)

class TestActionBooleanD(TestActionBoolean):
    def setUp(self):
        TestActionBoolean.onlyDockerTest()
        TestActionBoolean.setUp(self)

class TestActionIntegerD(TestActionInteger):
    def setUp(self):
        TestActionInteger.onlyDockerTest()
        TestActionInteger.setUp(self)

class TestActionSwitchBinaryD(TestActionSwitchBinary):
    def setUp(self):
        TestActionSwitchBinary.onlyDockerTest()
        TestActionSwitchBinary.setUp(self)

class TestActionSwitchMultilevelD(TestActionSwitchMultilevel):
    def setUp(self):
        TestActionSwitchMultilevel.onlyDockerTest()
        TestActionSwitchMultilevel.setUp(self)

class TestActionShutterBinaryD(TestActionShutterBinary):
    def setUp(self):
        TestActionShutterBinary.onlyDockerTest()
        TestActionShutterBinary.setUp(self)

class TestActionShutterMultilevelD(TestActionShutterMultilevel):
    def setUp(self):
        TestActionShutterMultilevel.onlyDockerTest()
        TestActionShutterMultilevel.setUp(self)

class TestActionButtonBinaryD(TestActionButtonBinary):
    def setUp(self):
        TestActionButtonBinary.onlyDockerTest()
        TestActionButtonBinary.setUp(self)

class TestActionButtonMultilevelD(TestActionButtonMultilevel):
    def setUp(self):
        TestActionButtonMultilevel.onlyDockerTest()
        TestActionButtonMultilevel.setUp(self)

from .test_values import TestListString

class TestListStringD(TestListString):
    def setUp(self):
        TestListString.onlyDockerTest()
        TestListString.setUp(self)

from .test_values import TestActionFsm

class TestActionFsmD(TestActionFsm):
    def setUp(self):
        TestActionFsm.onlyDockerTest()
        TestActionFsm.setUp(self)

from .test_values_basic import TestSensorFloat, TestSensorByte, TestSensorInteger

class TestSensorFloatD(TestSensorFloat):
    def setUp(self):
        TestSensorFloat.onlyDockerTest()
        TestSensorFloat.setUp(self)

class TestSensorByteD(TestSensorByte):
    def setUp(self):
        TestSensorByte.onlyDockerTest()
        TestSensorByte.setUp(self)

class TestSensorIntegerD(TestSensorInteger):
    def setUp(self):
        TestSensorInteger.onlyDockerTest()
        TestSensorInteger.setUp(self)

from .test_values_config import TestConfigString, TestConfigPassword, TestConfigInteger, TestConfigByte
from .test_values_config import TestConfigList, TestConfigArray, TestConfigBoolean, TestConfigFloat

class TestConfigStringD(TestConfigString):
    def setUp(self):
        TestConfigString.onlyDockerTest()
        TestConfigString.setUp(self)

class TestConfigPasswordD(TestConfigPassword):
    def setUp(self):
        TestConfigPassword.onlyDockerTest()
        TestConfigPassword.setUp(self)

class TestConfigIntegerD(TestConfigInteger):
    def setUp(self):
        TestConfigInteger.onlyDockerTest()
        TestConfigInteger.setUp(self)

class TestConfigByteD(TestConfigByte):
    def setUp(self):
        TestConfigByte.onlyDockerTest()
        TestConfigByte.setUp(self)

class TestConfigListD(TestConfigList):
    def setUp(self):
        TestConfigList.onlyDockerTest()
        TestConfigList.setUp(self)

class TestConfigArrayD(TestConfigArray):
    def setUp(self):
        TestConfigArray.onlyDockerTest()
        TestConfigArray.setUp(self)

class TestConfigBooleanD(TestConfigBoolean):
    def setUp(self):
        TestConfigBoolean.onlyDockerTest()
        TestConfigBoolean.setUp(self)

class TestConfigFloatD(TestConfigFloat):
    def setUp(self):
        TestConfigFloat.onlyDockerTest()
        TestConfigFloat.setUp(self)

from .test_values_sensors import TestSensorTemperature, TestSensorAltitude, TestSensorVoltage, TestSensorCurrent
from .test_values_sensors import TestSensorPercent, TestSensorFrequency, TestSensorHumidity, TestSensorPressure

class TestSensorTemperatureD(TestSensorTemperature):
    def setUp(self):
        TestSensorTemperature.onlyDockerTest()
        TestSensorTemperature.setUp(self)

class TestSensorAltitudeD(TestSensorAltitude):
    def setUp(self):
        TestSensorAltitude.onlyDockerTest()
        TestSensorAltitude.setUp(self)

class TestSensorVoltageD(TestSensorVoltage):
    def setUp(self):
        TestSensorVoltage.onlyDockerTest()
        TestSensorVoltage.setUp(self)

class TestSensorCurrentD(TestSensorCurrent):
    def setUp(self):
        TestSensorCurrent.onlyDockerTest()
        TestSensorCurrent.setUp(self)

class TestSensorPercentD(TestSensorPercent):
    def setUp(self):
        TestSensorPercent.onlyDockerTest()
        TestSensorPercent.setUp(self)

class TestSensorFrequencyD(TestSensorFrequency):
    def setUp(self):
        TestSensorFrequency.onlyDockerTest()
        TestSensorFrequency.setUp(self)

class TestSensorHumidityD(TestSensorHumidity):
    def setUp(self):
        TestSensorHumidity.onlyDockerTest()
        TestSensorHumidity.setUp(self)

class TestSensorPressureD(TestSensorPressure):
    def setUp(self):
        TestSensorPressure.onlyDockerTest()
        TestSensorPressure.setUp(self)

from .test_values_sensors import TestSensorDistance, TestSensorRotationSpeed, TestSensorString, TestSensorFloat
from .test_values_sensors import TestSensorList, TestSensorByte, TestSensorInteger, TestSensorMemory

class TestSensorDistanceD(TestSensorDistance):
    def setUp(self):
        TestSensorDistance.onlyDockerTest()
        TestSensorDistance.setUp(self)

class TestSensorRotationSpeedD(TestSensorRotationSpeed):
    def setUp(self):
        TestSensorRotationSpeed.onlyDockerTest()
        TestSensorRotationSpeed.setUp(self)

class TestSensorStringD(TestSensorString):
    def setUp(self):
        TestSensorString.onlyDockerTest()
        TestSensorString.setUp(self)

class TestSensorFloatD(TestSensorFloat):
    def setUp(self):
        TestSensorFloat.onlyDockerTest()
        TestSensorFloat.setUp(self)

class TestSensorListD(TestSensorList):
    def setUp(self):
        TestSensorList.onlyDockerTest()
        TestSensorList.setUp(self)

class TestSensorByteD(TestSensorByte):
    def setUp(self):
        TestSensorByte.onlyDockerTest()
        TestSensorByte.setUp(self)

class TestSensorIntegerD(TestSensorInteger):
    def setUp(self):
        TestSensorInteger.onlyDockerTest()
        TestSensorInteger.setUp(self)

class TestSensorMemoryD(TestSensorMemory):
    def setUp(self):
        TestSensorMemory.onlyDockerTest()
        TestSensorMemory.setUp(self)

from .test_values_sensors import TestSensorOrientation, TestSensorPresence, TestSensorRainTotal, TestSensorRainRate
from .test_values_sensors import TestSensorWindDirection, TestSensorWindAverage, TestSensorWindGust

class TestSensorOrientationD(TestSensorOrientation):
    def setUp(self):
        TestSensorOrientation.onlyDockerTest()
        TestSensorOrientation.setUp(self)

class TestSensorPresenceD(TestSensorPresence):
    def setUp(self):
        TestSensorPresence.onlyDockerTest()
        TestSensorPresence.setUp(self)

class TestSensorRainTotalD(TestSensorRainTotal):
    def setUp(self):
        TestSensorRainTotal.onlyDockerTest()
        TestSensorRainTotal.setUp(self)

class TestSensorRainRateD(TestSensorRainRate):
    def setUp(self):
        TestSensorRainRate.onlyDockerTest()
        TestSensorRainRate.setUp(self)

class TestSensorWindDirectionD(TestSensorWindDirection):
    def setUp(self):
        TestSensorWindDirection.onlyDockerTest()
        TestSensorWindDirection.setUp(self)

class TestSensorWindAverageD(TestSensorWindAverage):
    def setUp(self):
        TestSensorWindAverage.onlyDockerTest()
        TestSensorWindAverage.setUp(self)

class TestSensorWindGustD(TestSensorWindGust):
    def setUp(self):
        TestSensorWindGust.onlyDockerTest()
        TestSensorWindGust.setUp(self)

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
