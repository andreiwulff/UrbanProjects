# class Human:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 	def say_info(self):
# 		den = Human('Denis', 22)
# 		max = Human('Max', 24)
# 		print(f'Hi, I am {self.name}, I am {self.age}')
# 		den.say_info()
	

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("No such a floor")


h1 = House('Condo Gorsky', 18)# Создание объектов House
h2 = House('Forest House', 2)


h1.go_to(5) #Вызов метода go_to
h2.go_to(10)
