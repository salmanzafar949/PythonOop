def Operator(type):
    def add(n, n1):
        return n + n1

    def sub(n, n1):
        return n - n1

    if type == "add":
        return add
    else:
        return sub


op = Operator('add')
op1 = Operator('sub')
print(op(4, 4))
print(op1(4, 4))
