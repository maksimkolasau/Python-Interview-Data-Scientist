class ToyClass:
    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = ToyClass()
print(obj.instancemethod())
print(ToyClass.instancemethod(obj))
print(obj.classmethod())
print(obj.staticmethod())
print(ToyClass.classmethod())
print(ToyClass.staticmethod())
print(ToyClass.instancemethod(self=1))

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('Sarah', 25)
person2 = Person.from_birth_year('Roark', 1994)

print(person1.name, person1.age)
print(person2.name, person2.age)
print(Person.is_adult(16))
