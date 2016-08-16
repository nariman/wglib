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

import struct


def parse_magic_number(raw):
    """
    :param raw: I/O stream for parse

    :return: Magic number
    :rtype: int
    """
    return struct.unpack("I", raw.read(4))[0]


def parse_block_count(raw):
    """
    :param raw: I/O stream for parse

    :return: Number of meta blocks in replay
    :rtype: int
    """
    return struct.unpack("I", raw.read(4))[0]


def parse_block(raw):
    """
    :param raw: I/O stream for parse

    :return: Tuple with block size and block content
    :rtype: tuple
    """
    size = struct.unpack("I", raw.read(4))[0]
    content = raw.read(size)
    return size, content


def parse_replay_meta(raw):
    """
    :param raw: I/O stream for parse

    :return: Tuple with replay meta
    :rtype: tuple
    """
    magic_number = parse_magic_number(raw)
    block_count = parse_block_count(raw)
    blocks = []

    for _ in range(block_count):
        blocks.append(parse_block(raw))

    return magic_number, block_count, blocks


def parse_replay_data(raw):
    """
    :param raw: I/O stream for parse

    :return: Encrypted and compressed replay data
    :rtype: bytes
    """
    return raw.read()


def parse_replay(raw):
    """
    :param raw: I/O stream for parse

    :return: Tuple with all replay content
    :rtype: tuple
    """
    return parse_replay_meta(raw), parse_replay_data(raw)
