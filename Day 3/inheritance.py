class Animal:
    def __init__(self):
        self.reproduce = True

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walks")


class Fish(Animal):
    def swim(self):
        print("swims")


elephant = Mammal()
elephant.eat()
print(elephant.reproduce)
