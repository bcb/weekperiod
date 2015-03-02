"""setup.py"""
#pylint:disable=line-too-long

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup #pylint:disable=import-error,no-name-in-module

setup(
    name='weekperiod',
    description='Divide the week into 28 periods.',
    author='Beau Barker',
    author_email='beauinmelbourne@gmail.com',
    packages=['weekperiod'],
    )
