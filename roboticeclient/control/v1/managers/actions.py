
"""
Manager for devices
"""

import sys
import six
import logging

import base

LOG = logging.getLogger(__name__)


class ActionManager(base.ControlManager):

    SCOPE = "action"

    def do(self, request, id):
        return self.request(
            '/{0}/{1}/do'.format(self.SCOPE, id),
            'POST')

actions = ActionManager()