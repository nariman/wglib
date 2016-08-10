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


def content(filename):
    return open(filename, 'r').read()


def splitlines(content):
    return [l.strip() for l in content.splitlines()]


long_description = content('README.md')
install_requires = splitlines(content('requirements.txt'))
tests_require = splitlines(content('requirements-test.txt'))

setup(
    name='wglib',
    version='2016.8.0',
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
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries'
    ),
)
