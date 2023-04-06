# # # text = input()
# # # words = text.split()
# # # text = '-'.join(words)
# # # print(text)
# #
# #
# # # text = '-'.join(input().split())
# # # print(text)
# #
# # # text = input().replace(' ', '-')
# # # print(text)
# #
# # # print(text := '-'.join(input().split()))
# #
# #
# # # number1 = int(input())
# # # number2 = int(input())
# # # number3 = int(input())
# # # average = round((number1 + number2 + number3) / 3, 3)
# #
# # number1 = float(input())
# # number2 = float(input())
# # number3 = float(input())
# # is_negative_number1 = number1 < 0
# # is_negative_number2 = number2 < 0
# # is_negative_number3 = number3 < 0
# # print(is_negative_number1 + is_negative_number2 + is_negative_number3)
#
#
# # number = -5
#
# # if number > 0:  # True
# #     print('number is positive')
# # elif number == 0:
# #     print('number is zero')
# # else:  # False
# #     print('number is negative')
#
# # number = 5
# #
# # is_even = 'No' if number % 2 else 'Yes'
# #
# # if number % 2:
# #     is_even = 'No'
# # else:
# #     is_even = 'Yes'
#
#
# # if condition1 or condition2 and condition3:
# #     pass
#
#
# # x = True
# # y = False
# # z = False
# # if not x or y:  # 0 + 0 = 0
# #     print(1)
# # elif not x or not y and z:  # 0 + 1 * 0 = 0 + 0 = 0
# #     print(2)
# # elif not x or y or not y and x:  # 0 + 0 + 1 * 1 = 0 + 0 + 1 = 1
# #     print(3)
# # else:
# #     print(4)
#
# # a = 5
# #
# # if isinstance(a, int | float):
# #     pass
#
# # if any():
# #     pass
#
#
# # numbers = [5, 'hello', 5, 7, 8]
# # print(numbers[1])
# # numbers[1] = 'good'
# # print(numbers)
#
# # numbers = [1, 2, 3, 4]
# # number = 4
# # print(numbers[3] is number)
#
#
# # list1 = [1, 2, 3]
# # list2 = [4, 5, 6, list1]
# # print(list2[3][1])
# # list1[0] = 10
# # print(list2)
#
# # objs = []
# # print(list('hello'))
#
# # numbers1 = [1, 2, 3]
# # numbers2 = [4, 5, 6]
# # print(numbers1 + numbers2)
# # print(numbers1 * 3)
#
# # numbers1 = [1, 2, 3]
# # numbers2 = numbers1
# # words = ['hello', 'java', 'python']
# # del words[1:]
# # print(words)
#
#
# # words = ['hello', 'java', 'python']
# # word = words.pop(1)
# # print(words)
# # print(word)
#
# words = ['hello', 'python', 'hello']
# # words.append([1, 2, 3, 4])
# words.insert(1, 'java')
# # words.remove('hello')
# print(words)


# objs = ['hello', 'python']
# objs.extend(['java', 'pycharm'])
# print(objs)


# numbers = [4, 5, 3, 6, 5, 7, 3, 5, 4]
# numbers.sort()
# print(numbers)

# words = ['Word', 'apple', 'Bread', 'age']
# result = sorted(words)
# print(result)
# words.sort(key=len, reverse=True)
# print(words)
# from copy import deepcopy
# objs1 = [1, 2, 3]
# objs2 = [4, 5, 6, objs1]
# objs3 = deepcopy(objs2)
# objs1.append(7)
# print(objs3)
# print(objs2)


# numbers = [0 for i in range(10)]
# print(numbers)


# numbers = (5, )
# print(numbers)

# objs = (5, 6, 7, [1, 2, 3, 4])
# objs[3].append(5)
# print(objs)


# numbers1 = (1, 2, 3, 4)
# numbers2 = [5, 6, 7, 8, 9]
# numbers3 = (*numbers1, *numbers2)
# print(numbers3)


# user = {
#     'first_name': 'Alex',
#     'last_name': 'Pupkin',
#     'email': 'vasya@pupkin.com',
#     'phone': '+375259145208',
#     'lang': ['ru', 'en']
# }
#
# print(user['email'])
# user['email'] = 'vasya@gmail.com'
# user['city'] = 'Minsk'
# print(user['lang'][1][1])

# data = dict.fromkeys(['name', 'email', 'city'])
# print(data)

# data = dict([('name', 'alex'), ('city', 'minsk')])
# print(data)


# data = {'name': 'Alex', 'age': 45}
# print(data.get('city', 'Minsk'))
# print(data.setdefault('city', 'Minsk'))
# print(data)
# print(data.pop('age', None))
# print(data.popitem())


# data = {'name': 'Alex', 'age': 45}
# print(list(data))
# new_data = {'age': 46, 'city': 'minsk'}
# result = {**data, **new_data}
# result = data | new_data  # +3.10
# print(result)
# data.update(new_data)
# print(data)


# print(set('hello'))

# data = {}

# print(frozenset({1, 2, 3, 4}))


# text = 'hello world'
# data = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


data = {
    0: {'name': 'alex', 'email': 'alex@gmail.com'},
    1: {'name': 'pavel', 'email': 'pavel@gmail.com'},
    2: {'name': 'misha', 'email': 'misha@gmail.com'},
}

# N = 44
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# 42 44


# TODO Написать генератор заполненного судоку, выполняется за <1 сек

# number = int(input())
is_even = 'No' if (number := int(input())) % 2 else 'Yes'
