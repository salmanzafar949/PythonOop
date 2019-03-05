class Payment:

    def __init__(self, price):
        self.__final_price = price + price * 0.5

    def getFinalPrice(self):
        return self.__final_price

    def setFinalPrice(self, discount):
        self.__final_price = self.__final_price - self.__CalculateDiscount(discount)

    def __CalculateDiscount(self,discount):
        return self.__final_price * (discount)/100

p = Payment(10)
p.setFinalPrice(100)
print(p.getFinalPrice())