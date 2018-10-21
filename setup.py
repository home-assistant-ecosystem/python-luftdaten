#!/usr/bin/env python3
"""
Copyright (c) 2017-2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

setup(
    name='luftdaten',
    version='0.3.2',
    description='Python API for interacting with luftdaten.info.',
    long_description=long_description,
    url='https://github.com/fabaff/python-luftdaten',
    download_url='https://github.com/fabaff/python-luftdaten/releases',
    author='Fabian Affolter',
    author_email='fabian@affolter-engineering.ch',
    license='MIT',
    install_requires=['aiohttp', 'async_timeout'],
    packages=['luftdaten'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
