"""
Wargaming API Python 3 Library
setup.

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

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


def content(filename, split_lines=False):
    c = open(filename, 'r').read()
    return c.splitlines() if split_lines else c


long_description = content('README.md')

install_requires = content('requirements.txt', split_lines=True)
tests_require = content('requirements-test.txt', split_lines=True)

setup(
    name='wglib',
    version='2016.12.1',
    description='Python library for Wargaming API',
    author='woofilee',
    author_email='woofilee@gmail.com',
    url='https://github.com/woofilee/wglib',
    long_description=long_description,
    license='MIT',
    packages=["wglib"],
    install_requires=install_requires,
    tests_require=install_requires + tests_require,
    test_suite="tests",
    cmdclass={
        'test': PyTest
    },
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries'
    ),
)
