
import requests
import logging
import json
import decimal

from requests.exceptions import Timeout

from .managers.actions import ActionManager
from .managers.devices import *
from .managers.systems import SystemManager
from .managers.locations import LocationManager
from .managers.plans import PlanManager
from .managers.hosts import HostManager
from .managers.const import ConstManager

from roboticeclient.common.client import BaseClient
from roboticeclient.common.manager import manager_factory

log = logging.getLogger(__name__)


def initialize(self):
    pass

def some_event(self):
    pass

subclass_body_dict = {
    "initialize": initialize,
    "some_event": some_event
}


class RoboticeControlClient(object):
    """
    if you want change base client for providing settings and some other stuff you can do this
    
    from roboticeclient.common.horizon import HorizonClient
    from roboticeclient.common.horizon import DjangoClient
    from roboticeclient.control.v1.base import RoboticeControlClient

    RoboticeControlClient.client_class = HorizonClient

    robotice_client = RoboticeControlClient(type="control", ...)
    """

    client_class = BaseClient

    manager_classes = [("actions", ActionManager),
                       ("systems", SystemManager),
                       ("real_devices", RealDeviceManager),
                       ("model_devices", ModelDeviceManager),
                       ("system_devices", SystemDeviceManager),
                       ("locations", LocationManager),
                       ("plans", PlanManager),
                       ("const", ConstManager),
                       ("devices", DevicesManager),
                       ("hosts", HostManager)]

    def init_managers(self, **kwargs):

        for manager in self.manager_classes:

            Manager = type(manager[1].__name__, (manager_factory(self.client_class), manager[1]), {
                "initialize": initialize,
                "some_event": some_event
            })
            setattr(self, manager[0], Manager(**kwargs))

        return True

    def __init__(self, **kwargs):
        self.init_managers(**kwargs)
