def curry(function):
    def curried(*args):
        if len(args) == function.__curry_argcount:
            return function(*args)

        def partial(*pargs):
            return function(*(args+pargs))

        partial.__curry_argcount = function.__curry_argcount - len(args)

        return curry(partial)

    try:
        curried.__curry_argcount = function.__curry_argcount
    except AttributeError:
        function.__curry_argcount = function.__code__.co_argcount
        curried.__curry_argcount = function.__curry_argcount

    return curried
