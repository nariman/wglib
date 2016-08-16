"""
Wargaming API Python 3 Library
wglib.replay.parser.

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

import io
import os.path
from wglib import exceptions, settings
from wglib.replay import parser, decoder


class Replay:
    def __init__(self, filename=None, raw=None,
                 replay_max_size=settings.REPLAY_MAX_SIZE):
        self._raw = ""

        if raw:
            self._raw = io.BytesIO(raw)
        elif filename:
            if os.path.isfile(filename):
                if os.path.getsize(filename) < replay_max_size:
                    self._raw = open(filename, "rb")
                else:
                    raise exceptions.WGLibError("Replay file is too large")
            else:
                raise exceptions.WGLibError("Replay file not found")
        else:
            raise exceptions.ValidationError(
                "Filename or raw data needed for replay parsing")

        self._magic_number = None
        self._block_count = None
        self._blocks = []
        self._replay_data = None

    def parse_replay_meta(self):
        self._magic_number, self._block_count, self._blocks = \
            parser.parse_replay_meta(self._raw)

    def parse_replay_data(self):
        if not self._magic_number:
            raise exceptions.WGLibError("Replay meta must be parsed first")

        self._replay_data = parser.parse_replay_data(self._raw)

    def parse_replay(self):
        self.parse_replay_meta()
        self.parse_replay_meta()
