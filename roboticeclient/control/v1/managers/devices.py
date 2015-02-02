
"""
Manager for devices
"""

import sys
import six
import logging

from . import base

LOG = logging.getLogger("devices")


class RealDeviceManager(base.BaseManager):

    SCOPE = "real-device"


class ModelDeviceManager(base.BaseManager):

    SCOPE = "model-device"


class SystemDeviceManager(base.BaseManager):

    SCOPE = "system-device"


class DevicesManager(base.BaseManager):

    SCOPE = "device-catalog"


class MetricManager(base.BaseManager):

    SCOPE = "device-catalog/metric/"
