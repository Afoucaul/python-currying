import unittest

import types
from curry import curry


def test_two_arguments():
    @curry
    def add(a, b):
        return a + b

    assert isinstance(add, types.FunctionType)
    assert isinstance(add(1), types.FunctionType)
    assert add(1, 2) == 3
    assert add(1)(2) == 3


def test_three_arguments():
    @curry
    def add(a, b, c):
        return a + b + c

    assert isinstance(add, types.FunctionType)
    assert isinstance(add(1), types.FunctionType)
    assert isinstance(add(1, 2), types.FunctionType)
    assert isinstance(add(1)(2), types.FunctionType)
    assert add(1, 2, 3) == 6
    assert add(1)(2, 3) == 6
    assert add(1, 2)(3) == 6
    assert add(1)(2)(3) == 6
