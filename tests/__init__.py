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

import unittest


LOGGING_FORMAT = "# %(levelname)-8s [%(asctime)s] %(filename)s@%(lineno)d: " \
                 "%(message)s"

# logger = logging.getLogger("wglib")
# logger.setLevel("DEBUG")
# logger_formatter = logging.Formatter(LOGGING_FORMAT)

# logger_console_handler = logging.StreamHandler()
# logger_console_handler.setFormatter(logger_formatter)

# logger_file_handler = logging.FileHandler("wglib.log")
# logger_file_handler.setFormatter(logger_formatter)

# logger.addHandler(logger_console_handler)
# logger.addHandler(logger_file_handler)


if __name__ == '__main__':
    unittest.main()
