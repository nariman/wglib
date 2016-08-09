"""
Wargaming API Python 3 Library
tests.

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

import logging
import unittest
import wglib
import wglib.exceptions

LOGGING_FORMAT = "# %(levelname)-8s [%(asctime)s] %(filename)s@%(lineno)d: " \
                 "%(message)s"

logger = logging.getLogger("wglib")
logger.setLevel("DEBUG")
logger_formatter = logging.Formatter(LOGGING_FORMAT)

logger_console_handler = logging.StreamHandler()
logger_console_handler.setFormatter(logger_formatter)

# logger_file_handler = logging.FileHandler("wglib.log")
# logger_file_handler.setFormatter(logger_formatter)

logger.addHandler(logger_console_handler)
# logger.addHandler(logger_file_handler)


class LibraryTestCase(unittest.TestCase):
    def test_api(self):
        wglib.WoT("demo", "ru")
        wglib.WoTB("demo", "ru")
        wglib.WoTX("demo", "xbox")
        wglib.WoWS("demo", "ru")
        wglib.WoWP("demo", "ru")
        wglib.WGN("demo", "ru")

    def test_api_language(self):
        wglib.WoT("demo", "ru", "ru")
        wglib.WoTB("demo", "ru", "ru")
        wglib.WoTX("demo", "xbox", "ru")
        wglib.WoWS("demo", "ru", "ru")
        wglib.WoWP("demo", "ru", "ru")
        wglib.WGN("demo", "ru", "ru")

    def test_api_wrong_realm(self):
        with self.assertRaises(wglib.exceptions.ValidationError):
            wglib.WoT("demo", "martian")

        with self.assertRaises(wglib.exceptions.ValidationError):
            wglib.WoT("demo", "mac")


class DataTestCase(unittest.TestCase):
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
