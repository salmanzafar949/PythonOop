class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dancer:
    def __init__(self, style):
        self.style = style


class Student(Human, Dancer):
    def __init__(self, name, age, style):
        Human.__init__(self, name, age)
        Dancer.__init__(self, style)


s = Student('salman', 24, 'Salsa')

print(s.style)
print(s.name)
print(s.age)