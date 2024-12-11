# class Human:
# 	def __init__(self, name, group):
# 		self.name = name
# 		super().__init__(group)
# 	def info(self):
# 		print(f'Hi, I am {self.name}')
# class StudentGroup:
# 	def __init__(self, group):
# 		self.group = group
# 	def about(self):
# 		print(f'{self.name} belongs to {self.group}')
# class Student(Human, StudentGroup):
# 	def __init__(self, name, place, group):
# 		super(). __init__(name, group)
# 		self.place = place
# 		super().info()
# human = Human('Dennis')
# print(human.name)
# student = Student('Max', 'Urban','Python 1')
# student.about()
# print(student)



import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")
    def speak(self):
        print(self.sound)
class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dz = abs(dz)
        if self._cords[2] - dz * (self.speed / 2) < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] -= dz * (self.speed / 2)
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)# Exemples
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

