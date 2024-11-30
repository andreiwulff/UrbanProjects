numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number > 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        else:
            not_primes.append(number)
    print(primes)
    print(not_primes)















# while True:
#     number = int(input('Enter a number'))
#     if number % 2 == 0:
#         print('Even')
#     else:
#         print("Odd")
#         print('I am nor forgotten')
#         print('I am behind the cycle')
#

# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#        print(i)
# print(list_)

# list_2 = [2, 3, 4, 5, 1, 7]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} ** {j} = {i ** j}')

# dict = {'a': 1, 'b': 2, 'c': 3}
# for i in dict:
#     print(i, dict[i])

# dict = {'a': 1, 'b': 2, 'c': 3}
# for i, k in dict.items():
#     print(i, k)