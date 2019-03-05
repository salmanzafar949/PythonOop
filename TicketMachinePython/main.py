from TicketMachinePython.Ticket import Ticket

class Main:
    def __init__(self):
        t = Ticket()
        t.method = 500
        self.price = t.CalculatePriceAndgenerateticket()

m = Main()
print(m.price)