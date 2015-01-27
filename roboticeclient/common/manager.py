
import os
import logging
import decimal

LOG = logging.getLogger("manager.base")


from roboticeclient.common.client import BaseClient

class BaseManager(BaseClient):

    api_prefix = '/api' # /api/v1 etc

    def list(self):
        return self.request(
            '/%s' % self.SCOPE,
            'GET')

    def get(self, request, id):
        return self.request(
            request,
            '/{0}/{1}/'.format(self.SCOPE, id),
            'GET')


    def create(self, request, id, data):
        return self.request(
            request,
            '/{0}/{1}/'.format(self.SCOPE, id),
            'POST',
            data)

    def update(self, request, id, data):
        return self.request(
            request,
            '/{0}/{1}/'.format(self.SCOPE, id),
            'PUT',
            data)

    def __init__(self, **kwargs):
            
        self.host = kwargs.pop("host", os.getenv('ROBOTICE_HOST', '127.0.0.1'))
        self.port = kwargs.pop("port", os.getenv('ROBOTICE_PORT', 9753))
        self.protocol = kwargs.pop("protocol", os.getenv('ROBOTICE_PROTOCOL', "http")) 
        self.set_api()