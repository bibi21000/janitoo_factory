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

from janitoo_nosetests import JNTTBase
from janitoo_nosetests.values import JNTTFactory, JNTTFactoryCommon, JNTTFactoryPollCommon, JNTTFactoryConfigCommon

from janitoo.runner import Runner, jnt_parse_args
from janitoo.server import JNTServer
from janitoo.options import JNTOptions

class TestSensorTemperature(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_temperature'

class TestSensorAltitude(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_altitude'

class TestSensorVoltage(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_voltage'

class TestSensorCurrent(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_current'

class TestSensorPercent(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_percent'

class TestSensorFrequency(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_frequency'

class TestSensorHumidity(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_humidity'

class TestSensorPressure(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_pressure'

class TestSensorDistance(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_distance'

class TestSensorRotationSpeed(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_rotation_speed'

class TestSensorString(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_string'

class TestSensorFloat(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_float'

class TestSensorList(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_list'

class TestSensorByte(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_byte'

class TestSensorInteger(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_integer'

class TestSensorMemory(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_memory'

class TestSensorOrientation(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_orientation'

class TestSensorPresence(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_presence'

class TestSensorRainTotal(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_rain_total'

class TestSensorRainRate(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_rain_rate'

class TestSensorWindDirection(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_wind_direction'

class TestSensorWindAverage(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_wind_average'

class TestSensorWindGust(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_wind_gust'

class TestSensorWindGust(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_wind_gust'

class TestSensorMinute(JNTTFactory, JNTTFactoryPollCommon):
    """Test the value factory
    """
    entry_name='sensor_minute'
