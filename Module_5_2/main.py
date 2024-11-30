class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('No such a floor')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Name: {self.name}, Number of floors: {self.number_of_floors}'
h1 = House('Condo Elbrus', 10)
h2 = House('Condo Acacia', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
h1.go_to(5)
h2.go_to(10)
h2.go_to(25)