
from __future__ import absolute_import

import requests
import logging
import json

from horizon import messages
from django.conf import settings

from roboticeclient.common.django import DjangoClient
from roboticeclient.utils.dotdict import list_to_dotdict

from roboticeclient.exceptions import Unauthorized, BadRequest, ClientException

LOG = logging.getLogger("client.base")

TOKEN_FORMAT = "  Token {0}"


class HorizonClient(DjangoClient):

    """use Openstack Horizon settings
    for configuration and provide some additional messages
    ROBOTICE_HOST default is localhost
    ROBOTICE_PORT default is 9753
    ROBOTICE_PROTOCOL default is http

    we use tenant_name as location
    """

    def __init__(self, **kwargs):
        super(HorizonClient, self).__init__(**kwargs)

        try:
            self.host = getattr(settings, 'ROBOTICE_HOST', 'localhost')
            self.port = getattr(settings, 'ROBOTICE_PORT', 9753)
        except Exception, e:
            LOG.error(str(e))

        self.set_api()

    def request(self, path, method="GET", params={}, request=None):
        headers = {}

        _request = request
        self.set_api()
        full_path = '%s%s' % (self.api, path)
        if not full_path.endswith("/"):
            full_path = full_path + '/'
        LOG.debug("%s - %s - %s" % (method, full_path, params))

        if _request and hasattr(_request.user, "location"):
            try:
                token = _request.session['token'].id
                headers["Authorization"] = TOKEN_FORMAT.format(token)
            except Exception, e:
                raise e

        if method == "GET":
            request = requests.get(full_path, headers=headers)
        elif method == "POST":
            headers["Content-Type"] = "application/json"
            request = requests.post(
                full_path, data=json.dumps(params), headers=headers)
        elif method == "PUT":
            headers["Content-Type"] = "application/json"
            request = requests.put(
                full_path, data=json.dumps(params), headers=headers)
        elif method == "DELETE":
            request = requests.delete(
                full_path, data=json.dumps(params), headers=headers)

        if request.status_code in (200, 201):
            result = request.json()
            if "error" in result:
                msg = result.get("error")
                # populate exception
                messages.error(_request, msg)
                if settings.DEBUG:
                    raise Exception(msg)
            else:
                converted_dict = list_to_dotdict(result)
                return converted_dict
            return result
        else:
            if getattr(settings, "DEBUG", False):
                msg = "url: %s%s, method: %s, status: %s" % (
                    self.api, path, method, request.status_code)
            else:
                msg = "Unexpected exception."
            if request.status_code == 401:
                raise Unauthorized
            if request.status_code == 400:
                raise BadRequest
            messages.error(_request, msg)
            raise ClientException("Unhandled response status %s" % request.status_code)

    def get_location(self, request):
        """must return location queue, for now tenant name will be used
        """
        return request.user.location
