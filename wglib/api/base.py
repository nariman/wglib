"""
Wargaming API Python 3 Library
wglib.api.base.

The MIT License (MIT)
Copyright (c) 2016 Nariman Safiulin
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import logging
import requests
from wglib import __version__, exceptions, settings

_logger = logging.getLogger(__name__)


class Request:
    def __init__(self, api, method, data=None):
        """
        :type api: :class:`wglib.api.base.API`
        :param api: API object
        :type method: str
        :param method: API method
        :type data: dict
        :param data: Method parameters
        """
        self._api = api
        self._method = method + "/"
        self._data = data if data else dict()

    def __getitem__(self, key):
        return self._data.get(key)

    def __setitem__(self, key, value):
        self._data[key] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getattr__(self, method):
        return Request(self._api, self._method + method)

    def __call__(self, **kwargs):
        self._data.update(kwargs)
        return self._api.request(self)

    @property
    def api(self):
        return self._api

    @property
    def method(self):
        return self._method

    @property
    def data(self):
        return self._data


class Response:
    def __init__(self, request, raw):
        self._raw = raw
        self._request = request
        self._data = json.loads(raw)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    @property
    def raw(self):
        return self._raw

    @property
    def request(self):
        return self._request

    @property
    def data(self):
        return self._data


class API:
    def __init__(self, api_name, application_id, realm, language=None):
        if realm not in settings.API_ENDPOINTS[api_name]:
            raise exceptions.ValidationError("Unknown realm")

        # self._api_name = api_name
        self._cluster = settings.API_ENDPOINTS[api_name][realm]
        self._global_parameters = dict()
        # self._realm = realm

        self["application_id"] = application_id

        # New languages can be added. Checks are not required.
        if language:
            self["language"] = language

        _logger.info("WG API created ({0}, {1}). Library version: {0}."
                     .format(api_name, realm, __version__))

    def __getattr__(self, method):
        return Request(self, method)

    def __getitem__(self, key):
        return self._global_parameters.get(key)

    def __setitem__(self, key, value):
        self._global_parameters[key] = value

    def __len__(self):
        return len(self._global_parameters)

    def __iter__(self):
        return iter(self._global_parameters)

    @property
    def global_parameters(self):
        return self._global_parameters

    def request(self, request):
        """
        :type request: :class:`wglib.api.base.Request`
        :param request: Request object

        :rtype: :class:`wglib.api.base.Response`
        :return: Response object
        """
        data = self._global_parameters.copy()
        data.update(request.data)

        return Response(request,
                        requests.post(self._cluster + request.method,
                                      data=data,
                                      headers={
                                          "User-Agent":
                                              settings.HTTP_USER_AGENT_HEADER}
                                      ).text)
