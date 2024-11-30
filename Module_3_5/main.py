# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
# print(summa(998))

stack = []
# stack.append(1)
# print('Item added', stack)
# stack.append(2)
# print('Item added', stack)
# stack.append(3)
# print('Item added', stack)
# print(stack)
# stack.pop()
# print('Item deleted', stack)
# stack.pop()
# print('Item deleted', stack)
# stack.pop()
# print('Item deleted', stack)
# print(stack)

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)
result = get_multiplied_digits(40203)
print(result)


