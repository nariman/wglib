"""
Wargaming API Python 3 Library
tests.test_api.test_requests.

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
import asynctest
import pytest
from wglib import api


class NonAsyncTestCase(unittest.TestCase):
    def test_api_global_parameters(self):
        parameters = {
            "application_id": "alpha",
            "language": "en",
            "test_parameter": "test_value",
        }

        wgn = api.WGN("demo", "ru", "ru")

        # Testing default values, reading parameters from api
        self.assertEqual(wgn["application_id"], "demo")
        self.assertEqual(wgn["language"], "ru")
        self.assertEqual(len(wgn), 2)

        # Testing another default + extra values on the same api,
        # setting parameters to api
        # + testing iteration on the api global parameters
        for k in parameters:
            wgn[k] = parameters[k]
        for k in wgn:
            self.assertEqual(wgn[k], parameters[k])

        self.assertEqual(len(wgn), len(parameters))
        self.assertEqual(wgn.global_parameters, parameters)

    def test_api_request_object(self):
        parameters = {
            "test_parameter_1": "test_value_1",
            "test_parameter_2": "test_value_2",
            "test_parameter_3": "test_value_3",
        }

        wgn = api.WGN("demo", "ru")

        request = wgn.servers.info
        self.assertEqual(wgn, request.api)

        for k in parameters:
            request[k] = parameters[k]
        for k in request:
            self.assertEqual(request[k], parameters[k])

        self.assertEqual(len(request), len(parameters))

    def test_requests(self):
        # R1: with attribute
        wgn = api.WGN("demo", "ru")
        self.assertEqual("ok", wgn.servers.info().data["status"])

        # R2: with dict-like behavior
        wot = api.WoT("demo", "ru")
        self.assertEqual("ok", wot.account.list(search="_WooFi_")["status"])

    def test_requests_with_error(self):
        # R1
        wot = api.WoT("demo", "ru")
        self.assertEqual("error", wot.account.list(search="").data["status"])

    def test_api_response_object(self):
        wgn = api.WGN("demo", "ru")
        request = wgn.servers.info
        response = request()

        self.assertEqual(request, response.request)
        self.assertEqual(len(response.data), len(response))
        self.assertIsInstance(response.raw, str)
        self.assertEqual(
            [k for k in iter(response.data)],
            [k for k in iter(response)]
        )


class AsyncTestCase(asynctest.TestCase):
    async def test_api_global_parameters(self):
        parameters = {
            "application_id": "alpha",
            "language": "en",
            "test_parameter": "test_value",
        }

        wgn = api.aio.WGN("demo", "ru", "ru")

        # Testing default values, reading parameters from api
        self.assertEqual(wgn["application_id"], "demo")
        self.assertEqual(wgn["language"], "ru")
        self.assertEqual(len(wgn), 2)

        # Testing another default + extra values on the same api,
        # setting parameters to api
        # + testing iteration on the api global parameters
        for k in parameters:
            wgn[k] = parameters[k]
        for k in wgn:
            self.assertEqual(wgn[k], parameters[k])

        self.assertEqual(len(wgn), len(parameters))
        self.assertEqual(wgn.global_parameters, parameters)

    async def test_api_request_object(self):
        parameters = {
            "test_parameter_1": "test_value_1",
            "test_parameter_2": "test_value_2",
            "test_parameter_3": "test_value_3",
        }

        wgn = api.aio.WGN("demo", "ru")

        request = wgn.servers.info
        self.assertEqual(wgn, request.api)

        for k in parameters:
            request[k] = parameters[k]
        for k in request:
            self.assertEqual(request[k], parameters[k])

        self.assertEqual(len(request), len(parameters))

    @pytest.mark.asyncio
    async def test_requests(self):
        # R1: with attribute
        wgn = api.aio.WGN("demo", "ru")
        self.assertEqual(
            "ok",
            (await wgn.servers.info()).data["status"]
        )

        # R2: with dict-like behavior
        wot = api.aio.WoT("demo", "ru")
        self.assertEqual(
            "ok",
            (await wot.account.list(search="_WooFi_"))["status"]
        )

    @pytest.mark.asyncio
    async def test_requests_with_error(self):
        # R1
        wot = api.aio.WoT("demo", "ru")
        self.assertEqual(
            "error",
            (await wot.account.list(search="")).data["status"]
        )

    @pytest.mark.asyncio
    async def test_api_response_object(self):
        wgn = api.aio.WGN("demo", "ru")
        request = wgn.servers.info
        response = await request()

        self.assertEqual(request, response.request)
        self.assertEqual(len(response.data), len(response))
        self.assertIsInstance(response.raw, str)
        self.assertEqual(
            [k for k in iter(response.data)],
            [k for k in iter(response)]
        )


if __name__ == '__main__':
    unittest.main()
