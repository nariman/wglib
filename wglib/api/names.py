"""
Wargaming API Python 3 Library
wglib.api.names.

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

from wglib.api import base


class WoT(base.API):
    def __init__(self, application_id, region, language=None):
        super().__init__("wot", application_id, region, language)


class WoTB(base.API):
    def __init__(self, application_id, region, language=None):
        super().__init__("wotb", application_id, region, language)


class WoTX(base.API):
    def __init__(self, application_id, platform, language=None):
        super().__init__("wotx", application_id, platform, language)


class WoWS(base.API):
    def __init__(self, application_id, region, language=None):
        super().__init__("wotb", application_id, region, language)


class WoWP(base.API):
    def __init__(self, application_id, region, language=None):
        super().__init__("wotb", application_id, region, language)


class WGN(base.API):
    def __init__(self, application_id, region, language=None):
        super().__init__("wgn", application_id, region, language)
