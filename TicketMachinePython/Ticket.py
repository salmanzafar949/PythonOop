class Ticket:
    def __init__(self):
        self.__ticket = ''

    @property
    def method(self):
        return self.__ticket

    @method.setter
    def method(self, price):
        self.__ticket = price

    @method.deleter
    def method(self):
        self.__ticket = ''

    def CalculatePriceAndgenerateticket(self):
        p = input('Enter number of tickets ')
        total_price = self.__ticket * int(p)
        return 'Total of ' + str(p) + ' tickets final price is ' + str(total_price)
