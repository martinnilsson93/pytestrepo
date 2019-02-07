import pytest

from . import true
from . import false


def test_true():
    assert true.this_is_true()


def test_false():
    assert not false.this_is_false()
