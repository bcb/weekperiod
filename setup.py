"""setup.py"""
#pylint:disable=line-too-long

import sys
from setuptools.command.test import test as TestCommand

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup #pylint:disable=import-error,no-name-in-module

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = '-v'
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

setup(
    name='weekperiod',
    description='Divide the week into 28 periods.',
    author='Beau Barker',
    author_email='beauinmelbourne@gmail.com',
    install_requires=['weekperiod'],
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    )
