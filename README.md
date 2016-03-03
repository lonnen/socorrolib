socorrolib
-----------

[![Build Status](https://travis-ci.org/mozilla/socorrolib.svg?branch=master)](https://travis-ci.org/mozilla/socorrolib)

The common library of the socorro crash reporter system.

Factoring out the common library is the first step to breaking up the mozilla/socorro monorepo, which contains multiple services as a historic quirk of Mozilla's development and deployment process.

Currently socorrolib is pinned to socorro revision:
1c485ce3e6e6b2839834ad8a9f184e407dc8c825

Eventually this relationship will invert and socorro should use standard import tools to pin a version of socorrolib.

## running tests

```
pip install --require-hashes -r requirements.txt

# all them tests
nosetests socorrolib

# with coverage
nosetests socorrolib --with-coverage --cover-html --cover-package=socorrolib

# to run a specific test
nostests socorrolib.unittest.external.test_crashstorage_base:TestCase.TestBase
```

## making a release

Travis-CI ships releases to pypi whenever a tag is pushed. You'll want to bump the version number in `setup.py` before you try that.
