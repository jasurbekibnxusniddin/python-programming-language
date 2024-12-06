class foo:
    def __init__(self):
        self.a = 100

class Dog:
    
    species = "Canis familiaris"

    def __init__(self, name, age, s):
        self.name = name
        self.age = age
        self.foo = "bar"
    
dog = Dog("Miles", 4, "foo")
print(dog.species)
print(dog.name)
print(dog.age)
print(dog.foo)

dog.species = "Canis lupus familiaris"
print(dog.species)

