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
from wglib.aio import api as aioapi


class NonAsyncTestCase(unittest.TestCase):
    def test_api_response_object(self):
        from wglib.api.base import Response

        wgn = api.WGN('demo', 'ru')
        request = wgn.servers.info
        response = request()

        self.assertIsInstance(response, Response)

        self.assertEqual(request, response.request)
        self.assertIsInstance(response.raw, str)

        # Case 1: attribute behavior
        self.assertEqual(response.data['status'], 'ok')

        # Case 2: dict-like behavior
        self.assertEqual(response['status'], 'ok')

        self.assertEqual(len(response.data), len(response))

        self.assertEqual(
            [k for k in iter(response.data)],
            [k for k in iter(response)]
        )

    def test_request_with_error(self):
        wot = api.WoT('demo', 'ru')

        self.assertEqual(
            wot.account.list(search='').data['status'],
            'error'
        )


class AsyncTestCase(asynctest.TestCase):
    @pytest.mark.asyncio
    async def test_api_response_object(self):
        from wglib.api.base import Response

        wgn = aioapi.WGN('demo', 'ru')
        request = wgn.servers.info
        response = await request()

        self.assertIsInstance(response, Response)

        self.assertEqual(request, response.request)
        self.assertIsInstance(response.raw, str)

        # Case 1: attribute behavior
        self.assertEqual(response.data['status'], 'ok')

        # Case 2: dict-like behavior
        self.assertEqual(response['status'], 'ok')

        self.assertEqual(len(response.data), len(response))

        self.assertEqual(
            [k for k in iter(response.data)],
            [k for k in iter(response)]
        )

    @pytest.mark.asyncio
    async def test_request_with_error(self):
        wot = aioapi.WoT('demo', 'ru')

        self.assertEqual(
            (await wot.account.list(search='')).data['status'],
            'error'
        )


if __name__ == '__main__':
    unittest.main()
