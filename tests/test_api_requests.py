"""
Wargaming API Python 3 Library
tests.test_api_requests.

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
import pytest
import wglib


class NonAsyncTestCase(unittest.TestCase):
    def test_wgn_servers_info(self):
        wgn = wglib.WGN("demo", "ru")

        self.assertEqual(
            wgn.servers.info().data["status"],
            "ok"
        )

    def test_wot_account_list(self):
        wot = wglib.WoT("demo", "ru")

        self.assertEqual(
            wot.account.list(search="_WooFi_").data["status"],
            "ok"
        )

    def test_wot_account_list_error(self):
        wot = wglib.WoT("demo", "ru")

        self.assertEqual(
            wot.account.list(search="").data["status"],
            "error"
        )


class AsyncTestCase(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_wgn_servers_info(self):
        wgn = wglib.AsyncIOWGN("demo", "ru")

        self.assertEqual(
            await wgn.servers.info().data["status"],
            "ok"
        )

    @pytest.mark.asyncio
    async def test_wot_account_list(self):
        wot = wglib.AsyncIOWoT("demo", "ru")

        self.assertEqual(
            await wot.account.list(search="_WooFi_").data["status"],
            "ok"
        )

    @pytest.mark.asyncio
    async def test_wot_account_list_error(self):
        wot = wglib.AsyncIOWoT("demo", "ru")

        self.assertEqual(
            await wot.account.list(search="").data["status"],
            "error"
        )


if __name__ == '__main__':
    unittest.main()
