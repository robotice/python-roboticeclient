
import os
import requests
import logging
import json
import decimal


LOG = logging.getLogger("robotice.client")

TOKEN_FORMAT = "  Token {0}"

from roboticeclient.common.manager import BaseManager


class ControlManager(BaseManager):

    api_prefix = '/api'  # /api/v1 etc

    def __init__(self, **kwargs):

        self.host = kwargs.pop("host", os.getenv('ROBOTICE_HOST', '127.0.0.1'))
        self.port = kwargs.pop("port", os.getenv('ROBOTICE_PORT', 9753))
        self.protocol = kwargs.pop(
            "protocol", os.getenv('ROBOTICE_PROTOCOL', "http"))
        self.set_api()
