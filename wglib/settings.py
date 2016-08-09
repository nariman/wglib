"""
Wargaming API Python 3 Library
wglib.

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

from wglib import __version__


API_LANGUAGES = ("en", "ru", "pl", "de", "fr", "es", "zh-cn", "tr", "cs", "th",
                 "vi", "ko")

API_SCOPES = ("wot", "wotb", "wotx", "wows", "wowp", "wgn", "wgpay")
API_ENDPOINTS = {
    "wot": {
        "asia": "https://api.worldoftanks.asia/wot/",
        "eu":   "https://api.worldoftanks.eu/wot/",
        "kr":   "https://api.worldoftanks.kr/wot/",
        "na":   "https://api.worldoftanks.com/wot/",
        "ru":   "https://api.worldoftanks.ru/wot/",
    },
    "wotb": {
        "asia": "https://api.wotblitz.asia/wotb/",
        "eu":   "https://api.wotblitz.eu/wotb/",
        "na":   "https://api.wotblitz.com/wotb/",
        "ru":   "https://api.wotblitz.ru/wotb/",
    },
    "wotx": {
        "ps4":  "https://api-ps4-console.worldoftanks.com/wotx/",
        "xbox": "https://api-xbox-console.worldoftanks.com/wotx/",
    },
    "wows": {
        "asia": "https://api.worldofwarships.asia/wows/",
        "eu":   "https://api.worldofwarships.eu/wows/",
        "kr":   "https://api.worldofwarships.kr/wows/",
        "na":   "https://api.worldofwarships.com/wows/",
        "ru":   "https://api.worldofwarships.ru/wows/",
    },
    "wowp": {
        "eu":   "https://api.worldofwarplanes.eu/wowp/",
        "na":   "https://api.worldofwarplanes.com/wowp/",
        "ru":   "https://api.worldofwarplanes.ru/wowp/",
    },
    "wgn": {
        "asia": "https://api.worldoftanks.asia/wgn/",
        "eu":   "https://api.worldoftanks.eu/wgn/",
        "kr":   "https://api.worldoftanks.kr/wgn/",
        "na":   "https://api.worldoftanks.com/wgn/",
        "ru":   "https://api.worldoftanks.ru/wgn/",
    },
}

HTTP_USER_AGENT_HEADER = 'wglib/{0} (https://github.com/woofilee/wglib)'.format(
    __version__)
