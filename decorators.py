def Add(func):
    def dummy(*args):
        b = 0
        for num in args:
            b = num + b
        return func('addition', b)

    return dummy


def Multiply(func):
    def dummy(*args):
        b = 1
        for num in args:
            b = num * b
        return func('multiplication', b)

    return dummy
