# def print_params(*, a=1, b=2, c=3):
#     print(a, b, c)
# print_params(a=1, b=2, c=3)

# def func_with_params(a, b=2, c=None):
#     if c is None:
#         c = []
#         c.append(a)
#     print(c)
#
# func_with_params(3)
# func_with_params(4)
# func_with_params(5)
# func_with_params(6)


def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [39, 'abracadabra', False]
values_dict = {'a':'100', 'b':'Problem', 'c': None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54, 32, 'Problem']
print_params(*values_list_2, 39)
