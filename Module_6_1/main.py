class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} ate {food.name}")
            self.fed = True
        else:
            print(f"{self.name} did not eat {food.name}")
            self.alive = False
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} ate {food.name}")
            self.fed = True
        else:
            print(f"{self.name} did not eat {food.name}")
            self.alive = False
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True
# Creating class objects
a1 = Predator('The Wolf of Wall Street')
a2 = Mammal('Hatiko')
p1 = Flower('A Seven-Color Flower')
p2 = Fruit('A clockwork Orange')
# Checking
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
