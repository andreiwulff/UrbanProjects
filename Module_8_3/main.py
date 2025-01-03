class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('INCORRECT VIN TYPE')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('INCORRECT VIN RANGE')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('INCORRECT DATA TYPE FOR NUMBERS')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('INCORRECT NUMBER LENGTH')
        return True

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} CREATED SUCCESSFULLY')

try:
    second = Car('Model2', 300, 'T001TP')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} CREATED SUCCESSFULLY')

try:
    third = Car('Model3', 2020202, 'NO NUMBER')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} CREATED SUCCESSFULLY')