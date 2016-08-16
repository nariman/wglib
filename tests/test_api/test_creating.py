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
from wglib import api
import wglib.exceptions


class NonAsyncTestCase(unittest.TestCase):
    def test_api(self):
        api.WoT("demo", "ru")
        api.WoTB("demo", "ru")
        api.WoTX("demo", "xbox")
        api.WoWS("demo", "ru")
        api.WoWP("demo", "ru")
        api.WGN("demo", "ru")

    def test_api_language(self):
        api.WoT("demo", "ru", "ru")
        api.WoTB("demo", "ru", "ru")
        api.WoTX("demo", "xbox", "ru")
        api.WoWS("demo", "ru", "ru")
        api.WoWP("demo", "ru", "ru")
        api.WGN("demo", "ru", "ru")

    def test_api_wrong_realm(self):
        with self.assertRaises(wglib.exceptions.ValidationError):
            api.WoT("demo", "martian")

        with self.assertRaises(wglib.exceptions.ValidationError):
            api.WoT("demo", "mac")


class AsyncTestCase(unittest.TestCase):
    def test_api(self):
        api.aio.WoT("demo", "ru")
        api.aio.WoTB("demo", "ru")
        api.aio.WoTX("demo", "xbox")
        api.aio.WoWS("demo", "ru")
        api.aio.WoWP("demo", "ru")
        api.aio.WGN("demo", "ru")

    def test_api_language(self):
        api.aio.WoT("demo", "ru", "ru")
        api.aio.WoTB("demo", "ru", "ru")
        api.aio.WoTX("demo", "xbox", "ru")
        api.aio.WoWS("demo", "ru", "ru")
        api.aio.WoWP("demo", "ru", "ru")
        api.aio.WGN("demo", "ru", "ru")

    def test_api_wrong_realm(self):
        with self.assertRaises(wglib.exceptions.ValidationError):
            api.aio.WoT("demo", "martian")

        with self.assertRaises(wglib.exceptions.ValidationError):
            api.aio.WoT("demo", "mac")


if __name__ == '__main__':
    unittest.main()
