#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup file of Janitoo
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

from os import name as os_name
from setuptools import setup, find_packages
from distutils.extension import Extension
from platform import system as platform_system
import glob
import os
import sys
from _version import janitoo_version

DEBIAN_PACKAGE = False
filtered_args = []

for arg in sys.argv:
    if arg == "--debian-package":
        DEBIAN_PACKAGE = True
    else:
        filtered_args.append(arg)
sys.argv = filtered_args

def data_files_config(res, rsrc, src, pattern):
    for root, dirs, fils in os.walk(src):
        if src == root:
            sub = []
            for fil in fils:
                sub.append(os.path.join(root,fil))
            res.append((rsrc, sub))
            for dire in dirs:
                    data_files_config(res, os.path.join(rsrc, dire), os.path.join(root, dire), pattern)

data_files = []
data_files_config(data_files, 'docs','src/docs/','*')

janitoo_entry_points = {
    "janitoo.threads": [
        "http = janitoo_factory.threads.http:make_thread",
        "email = janitoo_factory.threads.email:make_thread",
        "scenes = janitoo_factory.threads.scenes:make_thread",
        "remote = janitoo_factory.threads.remote:make_thread",
    ],
    "janitoo.components": [
        "scenes.scene = janitoo_factory.threads.scenes:make_scene",
        "http.resource = janitoo_factory.threads.http:make_http_resource",
        "remote.node = janitoo_factory.threads.remote:make_remote_node",
    ],
    "janitoo.values": [
        "rread_value = janitoo_factory.values.other:make_value_rread",
        "rwrite_value = janitoo_factory.values.other:make_value_rwrite",
        "sensor_pressure = janitoo_factory.values.sensor:make_sensor_pressure",
        "sensor_temperature = janitoo_factory.values.sensor:make_sensor_temperature",
        "sensor_altitude = janitoo_factory.values.sensor:make_sensor_altitude",
        "sensor_voltage = janitoo_factory.values.sensor:make_sensor_voltage",
        "sensor_float = janitoo_factory.values.sensor:make_sensor_float",
        "sensor_current = janitoo_factory.values.sensor:make_sensor_current",
        "sensor_percent = janitoo_factory.values.sensor:make_sensor_percent",
        "sensor_distance = janitoo_factory.values.sensor:make_sensor_distance",
        "sensor_frequency = janitoo_factory.values.sensor:make_sensor_frequency",
        "sensor_humidity = janitoo_factory.values.sensor:make_sensor_humidity",
        "sensor_rotation_speed = janitoo_factory.values.sensor:make_sensor_rotation_speed",
        "sensor_string = janitoo_factory.values.sensor:make_sensor_string",
        "sensor_list = janitoo_factory.values.sensor:make_sensor_list",
        "sensor_integer = janitoo_factory.values.sensor:make_sensor_integer",
        "sensor_byte = janitoo_factory.values.sensor:make_sensor_byte",
        "sensor_orientation = janitoo_factory.values.sensor:make_sensor_orientation",
        "sensor_memory = janitoo_factory.values.sensor:make_sensor_memory",
        "sensor_boolean = janitoo_factory.values.sensor:make_sensor_boolean",
        "sensor_presence = janitoo_factory.values.sensor:make_sensor_presence",
        "config_array = janitoo_factory.values.config:make_config_array",
        "config_boolean = janitoo_factory.values.config:make_config_boolean",
        "config_string = janitoo_factory.values.config:make_config_string",
        "config_password = janitoo_factory.values.config:make_config_password",
        "config_byte = janitoo_factory.values.config:make_config_byte",
        "config_integer = janitoo_factory.values.config:make_config_integer",
        "config_list = janitoo_factory.values.config:make_config_list",
        "config_float = janitoo_factory.values.config:make_config_float",
        "action_string = janitoo_factory.values.action:make_action_string",
        "action_byte = janitoo_factory.values.action:make_action_byte",
        "action_integer = janitoo_factory.values.action:make_action_integer",
        "action_list = janitoo_factory.values.action:make_action_list",
        "action_switch_binary = janitoo_factory.values.action:make_action_switch_binary",
        "action_switch_multilevel = janitoo_factory.values.action:make_action_switch_multilevel",
        "action_shutter_binary = janitoo_factory.values.action:make_action_shutter_binary",
        "action_shutter_multilevel = janitoo_factory.values.action:make_action_shutter_multilevel",
        "action_button_binary = janitoo_factory.values.action:make_action_button_binary",
        "action_button_multilevel = janitoo_factory.values.action:make_action_button_multilevel",
        "action_boolean = janitoo_factory.values.action:make_action_boolean",
        "transition_fsm = janitoo_factory.values.action:make_transition_fsm",
        "sensor_basic_float = janitoo_factory.values.basic:make_sensor_float",
        "sensor_basic_integer = janitoo_factory.values.basic:make_sensor_integer",
        "sensor_basic_byte = janitoo_factory.values.basic:make_sensor_byte",
    ],
}

setup(
    name = 'janitoo_factory',
    description = "The values, components and threads factory for Janitoo",
    author='Sébastien GALLET aka bibi2100 <bibi21000@gmail.com>',
    author_email='bibi21000@gmail.com',
    license = """
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
    """,
    url='http://bibi21000.gallet.info/',
    version = janitoo_version,
    zip_safe = False,
    packages = find_packages('src', exclude=["scripts", "docs", "config"]),
    include_package_data=True,
    data_files = data_files,
    package_dir = { '': 'src' },
    keywords = "core, official",
    install_requires=[
                     'janitoo',
                    ],
    tests_require=['janitoo_nosetests'],
    dependency_links = [
      'https://github.com/bibi21000/janitoo/archive/master.zip#egg=janitoo',
    ],
    entry_points = janitoo_entry_points,
)
