"""
These functions simulate synchronous interfaces for reading values from various sensors.
This may seem unrealistic, but sometimes you have to work with interfaces like this.

Don't change this file.
"""

import random
import time


def get_gps_data():
    time.sleep(1)
    return random.random()


def get_camera_data():
    time.sleep(0.1)
    return random.random()


def get_accelerometer_data():
    time.sleep(0.01)
    return random.random()
