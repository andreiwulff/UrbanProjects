def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        return total_sum / count if count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('Incorrect data type written in numbers')
        return None

print(f'Result 1: {calculate_average("1, 2, 3")}')
print(f'Result 2: {calculate_average([1, "String", 3, " one more string"])}')
print(f'Result 3: {calculate_average(567)}')
print(f'Result 4: {calculate_average([42, 15, 36, 13])}')
