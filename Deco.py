from decorators import Add, Multiply


@Multiply
def Operation(op, res):
    return op + ' gives result as ' + str(res)


print(Operation(2, 2))
