import socorrolib

from nose.tools import ok_
from skip_if import skip_if

__all__ = ['skip_if']

def test_should_have_version():
    ok_(socorrolib.__version__)
