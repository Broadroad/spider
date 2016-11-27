#-*- coding:utf-8 -*-
from __future__ import print_function
import gevent
from gevent import monkey
import re
import requests
from requests.exceptions import (RequestException, MissingSchema,
            InvalidSchema, InvalidURL)
from requests import Response, Request

"""Spawn multiple workers and wait for them to complete"""

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()


absolute_http_url_regexp = re.compile(r"^https?://", re.I)

class KirinResponse(Response):
    def raise_for_status(self):
        if hasattr(self, 'error') and self.error:
            raise self.error
        Response.raise_for_status(self)

class KirinRequest():
    def __init__(self, base_url, method='GET', params=None ,headers=None):
        self.base_url = base_url
        self.method = str(method).upper()
        self.params = params
        self.headers = headers
        
    def request(self):
        return self._send_request_safe_mode()
    def _send_request_safe_mode(self):
         """
         Send an HTTP request, and catch any exception that might occur due to connection problems.
         """
         try:
            if self.method == 'GET':
                return requests.get(self.base_url, params=self.params, headers=self.headers)
            elif self.method == 'POST':
                return requests.post(self.base_url, data=self.params, headers=self.headers)
         except (MissingSchema, InvalidSchema, InvalidURL):
            raise
         except RequestException as e:
            r = KirinResponse()
            r.error = e
            r.status_code = 0
            r.request = Request(self.method, self.base_url).prepare() 
            return r
        
