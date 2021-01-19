# __str__ this method returns the string representation of an object.
# __repr__ this method returns the object representation in string format.

class NamedPerson:

    def __init__(self, name_person, age_person):
        self.name = name_person
        self.age = age_person

    def __str__(self):
        return f'Name of the person is {self.name} and he has aged {self.age} years.'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p = NamedPerson('Pankaj', 34)

print(p.__str__())
print(p.__repr__())
