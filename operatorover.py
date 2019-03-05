class Book:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return  self.price + other.price

    def __lt__(self, other):
        return self.price < other.price

b = Book(500)
b1 = Book(450)

total_price = b + b1
compare  = b < b1
print(total_price)
print(compare)