# Python Currying

This module mainly consists in a decorator, `curry`, that curries a function.

## Currying?

The currying operation can be seen as making a function partially callable.
For instance, let's have an `add` function:

    >>> def add(a, b):
    ...     return a + b

Expectedly enough, `add(1, 2)` returns `3`.
However, `add(1)` raises an error:

    >>> add(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      TypeError: add() missing 1 required positional argument: 'b'

The goal of currying is to treat `add(1)` as a function of one parameter `x`, that returns the sum
of `1` and `x`.


## How it works

It's just a decorator, that will curry the function.

    >>> @curry
    ... def add(a, b):
    ...     return a + b
    ... 
    >>> add(1)
    <function curry.<locals>.curried at 0x7f2a17dc8d08>
    >>> add(1)(2)
    3
