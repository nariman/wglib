"""
Wargaming API Python 3 Library
tests.test_api.test_creating.

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

import unittest

import wglib.exceptions
from wglib import settings
from wglib import api as bioapi  # blocking i/o
from wglib.aio import api as aioapi  # async i/o


class TestCase(unittest.TestCase):
    def test_api(self):
        for api in [bioapi, aioapi]:
            api.WoT('demo', 'ru')
            api.WoTB('demo', 'ru')
            api.WoTX('demo', 'xbox')
            api.WoWS('demo', 'ru')
            api.WoWP('demo', 'ru')
            api.WGN('demo', 'ru')

    def test_api_language(self):
        for api in [bioapi, aioapi]:
            api.WoT('demo', 'ru', language='ru')
            api.WoTB('demo', 'ru', language='ru')
            api.WoTX('demo', 'xbox', language='ru')
            api.WoWS('demo', 'ru', language='ru')
            api.WoWP('demo', 'ru', language='ru')
            api.WGN('demo', 'ru', language='ru')

    def test_api_wrong_realm(self):
        for api in [bioapi, aioapi]:
            with self.assertRaises(wglib.exceptions.ValidationError):
                api.WoT('demo', 'antarctica')

            with self.assertRaises(wglib.exceptions.ValidationError):
                api.WoTX('demo', 'mac')

    def test_api_global_parameters(self):
        for api in [bioapi, aioapi]:
            pre = {
                'application_id': 'demo',
                'language': 'ru',
            }

            post = {
                'application_id': 'alpha',
                'language': 'en',
                'test_parameter': 'test_value',
            }

            headers = {
                'header_1': 'value_1',
                'header_2': 'value_2'
            }

            wgn = api.WGN(pre['application_id'], 'ru', language=pre['language'])

            # Testing default values, reading parameters from api

            self.assertEqual(wgn.global_parameters, pre)
            self.assertEqual(len(wgn), len(pre))

            for k in pre:
                self.assertEqual(wgn[k], pre[k])

            for k in wgn:
                self.assertEqual(wgn[k], pre[k])

            # Testing another default + extra values on the same api,
            # setting parameters to api

            for k in post:
                wgn[k] = post[k]

            self.assertEqual(wgn.global_parameters, post)
            self.assertEqual(len(wgn), len(post))

            for k in post:
                self.assertEqual(wgn[k], post[k])

            for k in wgn:
                self.assertEqual(wgn[k], post[k])

            # Default headers

            self.assertEqual(
                wgn.headers['User-Agent'],
                settings.HTTP_USER_AGENT_HEADER
            )

            for k in headers:
                wgn.headers[k] = headers[k]

            for k in headers:
                self.assertEqual(wgn.headers[k], headers[k])

    def test_api_request_object(self):
        from wglib.api.base import Request

        for api in [bioapi, aioapi]:
            parameters = {
                'parameter_1': 'value_1',
                'parameter_2': 'value_2',
                'parameter_3': 'value_3',
            }

            headers = {
                'header_1': 'value_1',
                'header_2': 'value_2'
            }

            wgn = api.WGN('demo', 'ru')
            request = wgn.servers.info

            self.assertIsInstance(request, Request)
            self.assertEqual(request.api, wgn)

            # Request parameters

            for k in parameters:
                request[k] = parameters[k]

            self.assertEqual(len(request), len(parameters))
            self.assertEqual(len(request.data), len(parameters))

            for k in parameters:
                self.assertEqual(request[k], parameters[k])
                self.assertEqual(request.data[k], parameters[k])

            for k in request:
                self.assertEqual(request[k], parameters[k])
                self.assertEqual(request.data[k], parameters[k])

            # Request headers

            for k in headers:
                request.headers[k] = headers[k]

            self.assertEqual(len(request.headers), len(headers))

            for k in headers:
                self.assertEqual(request.headers[k], headers[k])


if __name__ == '__main__':
    unittest.main()
