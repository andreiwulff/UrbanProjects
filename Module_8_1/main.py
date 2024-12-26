def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'STRING'))
print(add_everything_up('TABLE', 4215))
print(add_everything_up(123.456, 7))