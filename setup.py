#!/usr/bin/env python3
"""Luftdaten Python Wrapper setup script."""
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="luftdaten",
    version="0.6.5",
    description="Python API for interacting with luftdaten.info.",
    long_description=long_description,
    url="https://github.com/home-assistant-ecosystem/python-luftdaten",
    download_url="https://github.com/home-assistant-ecosystem/python-luftdaten/releases",
    author="Fabian Affolter",
    author_email="fabian@affolter-engineering.ch",
    license="MIT",
    install_requires=["aiohttp>=3.7.4,<4", "async_timeout<4"],
    packages=["luftdaten"],
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
