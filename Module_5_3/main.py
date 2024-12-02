class Building:
    total = 0
    def __init__(self):
        Building.total += 1
for i in range(40):
    building = Building()
    print(building)
class House(Building):
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance
    def __init__(self, name, floors):
        super().__init__()
        self.name = name
        self.floors = floors
    def __del__(self):
        print(f"{self.name} knocked down but remains in history")
h1 = House('Condo Elbrus', 10)
print(House.houses_history)
h2 = House('Condo Acacia', 20)
print(House.houses_history)
h3 = House('Condo Dolls', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)