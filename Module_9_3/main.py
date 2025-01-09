# Даны два списка
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк в одинаковых позициях без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример выполнения кода
print(list(first_result))
print(list(second_result))
