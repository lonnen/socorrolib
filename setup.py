"""
module installation information
"""

import codecs
import os
from setuptools import setup, find_packages


# Prevent spurious errors during `python setup.py test`, a la
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html:
try:
    # pylint: disable=W0611,C0411
    import multiprocessing
except ImportError:
    pass


def read(fname):
    """
    utility function to read and return file contents
    """
    fpath = os.path.join(os.path.dirname(__file__), fname)
    with codecs.open(fpath, 'r', 'utf8') as fhandle:
        return fhandle.read().strip()


setup(
    name="socorrolib",
    version="0.0.1",
    description="the common library of the socorro crash reporter",
    license="MPL-2",
    author="mozilla socorro team and friends",
    packages=find_packages(),
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
    ],
    test_suite='nose.collector',
)
