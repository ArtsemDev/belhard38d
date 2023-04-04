# # print('hello world')
# # print('hello python')
#
#
# # text = 'qwerty'
# # print(text[::-2])
#
#
# # text = 'hello'
# # a = len(text)
# # print(text[a])
#
# # text = 'hello'
# # print(text[:100])
#
#
# # name = 'Alex'
# # age = 34
#
# # text = 'Hello %s(a), your age %d(b)' % {'b': age, 'a': name}
# # text = 'Hello {a}, your age {b}'.format(b=name, a=age)
# # text = f'Hello {name}, your age {age * 2}'
# # print(text)
#
#
# # text = 'hello | world | python'
# # words = text.split(' | ')
# # print(words)
# # text2 = ' separator '.join(words)
# # print(text2)
#
#
# # text = 'Hello python world python great!'
# # result = text.replace('python', 'питон', 1)
# # print(result)
#
#
# # text = 'hello'
# # print(text.isalpha())
# # print(text.isdigit())
# # print(text.isascii())
# # print(text.isalnum())
# # print(text.isspace())
# # print(text.isprintable())
# # print(text.isidentifier())
#
# # print(float('-.5'))
# # print(float('nan'))
# # print(float('inf'))
#
# # print(round(3.14159, 3))
# # print(round(23.5))
# # print(round(24.5))
#
# # text = 'Hello Python'
# # print(text.startswith('Hell'))
#
#
# # text = 'hello world python world pycharm'
# # print(text.find('world'))
# # print(text.rfind('world'))
# # print(text.index('world'))
# # print(text.rindex('world'))
# # print(text.count('world', 0, 12))
# # print(text.partition('W'))
# # print(text.rpartition('W'))
#
# # from os import system
# # from time import sleep
# #
# # text = 'HeLlO wOrLd'
# # while True:
# #     print(text)
# #     sleep(1)
# #     text = text.swapcase()
# #     system('cls')
#
# # text = 'Helloß'
# # print(text.swapcase())
#
# # text = 'hello\tworld\tpythoneeeeeeee\tpycharm'
# # print(text.expandtabs(12))
#
# # text = '.-,--,.hello---world---,.,.,.'
# # print(text.lstrip('.,-'))
# # print(text.rstrip('.,-'))
# # print(text.strip('.,-'))
# # text = 'hello python'
# # print(text.removeprefix('hell'))
# # print(text.removesuffix('hon'))
#
# # text = 'hello'
# # print(text.center(4))
# # print(text.ljust(10))
# # print(text.rjust(10))
# # print(text.zfill(10))
#
# # num = bin(14)
# # print(num[2:].zfill(16))
# # print(bin(10))
# # print(bin(12))
# # print(10 ^ 12)
# # print(bin(6))
# # print(~-5)
# # print(~10)
#
# # print(bin(10))
# # print(bin(-11))
# # print(15 >> 2)
#
# # text = 'PYTHON'
# # print(text[1])
# # print(text[~1])
# # a = 4
# # b = round((a ** 2) ** 0.5)
# # print(a is b)
# # print(id(a))
# # print(id(b))
#
# # a = 0.3
# # b = round(0.1 * 3, 1)
# # print(a)
# # print(b)
# # print(a is b)
# # print(id(a))
# # print(id(b))
#
#
# # TODO Вводится строка (input), состоящая минимум из 3х слов
# #  необходимо переставить местами первое и последнее слово и записать
# #  в новую переменную
# #  HELLO WORLD PYTHON
# text = input('enter text: ')
#
# words = text.split()
# words[0], words[-1] = words[-1], words[0]
# result = ' '.join(words)
# # first_space = text.find(' ')
# # last_space = text.rfind(' ')
# #
# # first_word = text[:first_space]
# # last_word = text[last_space+1:]
# # center = text[first_space:last_space+1]
# #
# # result = last_word + center + first_word
# print(result)


# first_name = input('Enter Name: ')
# last_name = input('Enter Surname: ')

# first_name, last_name = input('Enter Name: '), input('Enter Surname: ')
# print(first_name)
# print(last_name)


# TODO Вводится слово, не учитывая регистр, вывести True, если слово
#  является палиндромом, и False в противном случае

# text = input('Enter word: ').lower()
# is_palindrome = text == text[::-1]
# print(is_palindrome)
# print(is_palindrome := ((word := input().lower()) == word[::-1]))


# TODO Вводится текст(text) и целое число(n) в разные переменные, необходимо
#  удалить символ из текста на индексе n
#  text = 'hello' n = 4 -> 'hell'

# text = input()
# n = int(input())
# result = text[:n] + text[n+1:]
# print(result)



# print('🔥'.encode('ascii', 'namereplace'))
# print('\N{fire}')
# print('🤣')

# n = int(input())
# print((n & (n-1) == 0) and n != 0)


# print('hello\nworld\npython'.count('\\'))
# text = 'hello' \
#        ' world' \
#        ' python'
#
# print(text)

# text = """
# hello
# world
# python
# """
# print(text.count('\n'))
#
# print(text)



