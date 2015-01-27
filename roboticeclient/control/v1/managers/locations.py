
"""
Manager for devices
"""

import sys
import six
import logging

import base

LOG = logging.getLogger("devices")


class LocationManager(base.ControlManager):

    SCOPE = "location"