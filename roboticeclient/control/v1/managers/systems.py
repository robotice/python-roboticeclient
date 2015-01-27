
"""
Manager for Systems systems.yml

"""

import sys
import six
import json
import logging

import base

LOG = logging.getLogger(__name__)


class SystemManager(base.ControlManager):

    SCOPE = "system"

systems = SystemManager()