"""
fail like skimage
"""

import sys

from setuptools import setup

if not 'sdist' in sys.argv:
    sys.exit('\n*** Please find and install the `socorro` package from src ***\n')

setup(
    name="socorrolib",
    version="0.2.4",
    author="mozilla socorro team and friends",
    url="https://github.com/mozilla/socorrolib",
    description="please find the `socorro` package and install from src",
    license="MPL-2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
    ],
)