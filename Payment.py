Methods = [
    'Paypal',
    'Cashier',
    'Payoneer'
]


# Property Decorators
class Payment:
    def __init__(self):
        self.__method = ''

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, met):
        if met in Methods:
            self.__method = met
        else:
            print('Invalid Method')

    @method.deleter
    def method(self):
        print('Deleting')
        self.__method = ''


p = Payment()
p.method = 'Paypal'
print(p.method)
del p.method
print(p.method)
