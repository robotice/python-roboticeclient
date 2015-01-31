
import os
import requests
import logging
import json
import decimal

from roboticeclient.common.client import BaseClient

LOG = logging.getLogger("client.base")

TOKEN_FORMAT = "  Token {0}"


class DjangoClient(BaseClient):

    """use django settings for configuration and provide some additional messages
    ROBOTICE_HOST default is localhost
    ROBOTICE_PORT default is 9753
    ROBOTICE_PROTOCOL default is http
    """

    api_prefix = '/api' # /api/v1 etc

    def __init__(self, **kwargs):
            
        try:
            from openstack_dashboard.local.local_settings import ROBOTICE_HOST, ROBOTICE_PORT
            self.host = ROBOTICE_HOST
            self.port = ROBOTICE_PORT
        except Exception, e:
            raise e

        self.set_api()

    def request(self, request, path, method="GET", params={}):
        headers = {}

        _request = request
        self.set_api(_request)
        log.debug("%s - %s%s - %s"%(method,self.api,path,params))
        
        headers["Location"] = self.get_location(_request)
        try:
            token = _request.session['token'].id
            headers["Authorization"] = TOKEN_FORMAT.format(token)
        except Exception, e:
            raise e

        if method == "GET":
            request = requests.get('%s%s' % (self.api, path), headers=headers)
        elif method == "POST":
            headers["Content-Type"] = "application/json"
            request = requests.post('%s%s' % (self.api, path),data=json.dumps(params, default=decimal_default),headers=headers)
        elif method == "PUT":
            headers["Content-Type"] = "application/json"
            request = requests.put('%s%s' % (self.api, path),data=json.dumps(params, default=decimal_default),headers=headers)
        elif method == "DELETE":
            request = requests.delete('%s%s' % (self.api, path),data=json.dumps(params, default=decimal_default),headers=headers)
        
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
                msg = "url: %s%s, method: %s, status: %s" % (self.api, path, method, request.status_code)
            else:
                msg = "Unexpected exception."
            messages.error(_request, msg)
            return []

    def list(self, request):
        return self.request(
            request,
            '/%s' % self.SCOPE,
            'GET')