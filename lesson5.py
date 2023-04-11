# 1
# numbers = [i**2 for i in range(int(input()))]


# 2
# text = input()
# data = {i: text.count(i) for i in set(text)}


# 3
# n = int(input())
# data = {
#     i: {
#         'name': input(f'name {i}: '),
#         'email': input(f'email {i}: ')
#     }
#     for i in range(n)
# }


# from collections import *


# text = 'hello world'
# data = Counter(text)
# text2 = 'hello python'
# data2 = Counter(text2)
# print(data)
# print(data2)
# print(data - data2)
# data.subtract(data2)
# print(data)
# print(data.most_common(2))
# print([*data.elements()])
# q = deque([1, 2, 3, 4, 5])
# data = defaultdict(list)
# data['age'].append(1)
# print(data['city'])
# print(data)


# keys = ('name', 'email', 'age')
#
# User = namedtuple('User', keys)
#
# vasya = User('vasya', 'vasya@gmail.com', 24)
# petya = User('petya', 'petya@gmail.com', 15)
# print(vasya)
# print(petya)

# is_break = False
# for i in range(1, 100):
#     if not i % 2:
#         continue
#
#     if i == 49:
#         # is_break = True
#         break
#
#     i **= 2
#     print(i)
# else:
#     print('finish')
# if not is_break:
#     print('finish')

# for number in range(100):
#     number **= 2
#     print(number)

# print(number)


# str, list, tuple, set, frozenset

# text = 'hello python'
# for el in text:
#     el = el.upper()
#     print(el)

# str, list, tuple
# for i in range(len(text)):
#     print(text[i])

# str list tuple
# for i, j in enumerate(text):
#     print(i, j, end=' ')

# dict
# data = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': 'value4',
#     'key5': 'value5',
#     'key6': 'value6',
# }
# for key in data:
#     print(key)

# for val in data.values():
#     print(val)

# for key, val in data.items():
#     print(key, val)

# for i in enumerate(data):
#     print(i)


# TODO Вводится число N, посчитать факториал N, N = 3 -> 1 * 2 * 3 = 6
#  (Найти произведение чисел от 1 до N включительно)


# N = int(input('N: '))
# factorial = 1
# for i in range(1, N+1):
#     factorial *= i
# print(factorial)


# TODO Вводится число N, посчитать сумму чисел от 0 до N включительно
# N = int(input())
# s = 0
# for i in range(1, N+1):
#     s += i


# TODO Заполнить список степенями числа 2 от 0 до N
# N = int(input())
# result = [2**i for i in range(N+1)]
# numbers = []
# for i in range(0, N+1):
#     numbers.append(2 ** i)
# print(numbers)
from dis import dis
# from timeit import timeit


# print(timeit('''text = 'hello world python '
# letters = []
# for letter in text:
#     if letter.isalpha():
#         letters.append(letter.upper())
# '''))

# print(timeit('''text = 'hello world python '
# letters = [element.upper() for element in text if element.isalpha()]
# '''))

# n = int(input())
# while n > 0:
#     n -= 1
#     print(n)

# TODO Спрашивать у пользователя данные с клавиатуры до тех пор пока
#  он не введет число
# while not (number := input()).isdigit(): ...

# number = input('Enter number: ')
# while not number.isdigit():
#     number = input('Are you stupid? Try again: ')

# TODO Вводится сумма депозита, процентная ставка
#  высчитать на какой год, депозит увеличиться в 2 раза
#  (вклад капитализации)

# deposit = 100
# target = deposit * 2
# percent = 10
# year = 0
# while deposit < target:
#     year += 1
#     deposit *= 1 + (percent / 100)
#     print(f'{year} Год: {deposit}')
# print(year)

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print('а или b не является числом')
# except ZeroDivisionError:
#     print('Делить на 0 нельзя')
# else:
#     print('Ошибок не было!')
# finally:
#     print('Выполняется в любом случае!')


# a = input()
# b = input()
# if not a.isdigit():
#     print('a not digit')
# if not b.isdigit():
#     print('b not digit')
# if b == 0:
#     print('zero division')
# a = int(a)
# b = int(b)
# c = a / b


# EAFP - Easier to Ask for Forgiveness than Permission

# print(len({True, False, 0, 1, 2, 3}))

# TODO Дан словарь, значениями которого могут быть любые типы данных
#  вывести ключи словаря, значениями которых являются числа

# data = {
#     'key1': 'hello',  # No
#     'key2': 333,  # Yes
#     'key3': [1, 2],  # No
#     'key4': 6789.8,  # Yes
#     'key5': True,  # No
#     'key6': None  # No
# }
# for key, value in data.items():
#     if isinstance(value, (int, float)) and not isinstance(value, bool):
#         print(key)


# result = [key for key, value in data.items() if isinstance(value, (int, float)) and not isinstance(value, bool)]


# data = {
#     1: 'First',
#     True: 'Second',
#     1.0: 'Third'
# }
# print(len(data))

# numbers = [1, 2, 3, 4, 5, 6]
# numbers2 = numbers[::-1]
# numbers2[0] = 456
# print(numbers[0])
# del numbers[::-1]
# print(numbers)

# text = 'Hello World'
# words = ['Hello', 'World']
# text2 = ' '.join(words)
# print(text is text2)
# text = 'Hello world'
# text2 = 'Hello world'
# print(text is text2)


# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a[0] is b[0])
