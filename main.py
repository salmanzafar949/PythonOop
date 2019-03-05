class Book:

    name = "NoteBook"

    def __init__(self):
        pass

    def SetName(self,name):
        self.name = name

    def GetName(self):
        return self.name


book1 = Book()
book2 = Book()

book1.SetName('The NoteBook')
book2.SetName('The NoteBook 2')

print(book1.GetName())
print(book2.GetName())