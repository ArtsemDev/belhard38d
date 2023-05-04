# # numbers = [1, 2, 3, 4]
# # print(*numbers)

# # numbers = [*range(1, 101)]
# # print(numbers)

# # numbers = '3.14'
# # a = 3.14

# # class A:
# # 	__name = 'A'

# # 	@classmethod
# # 	def bar(cls):
# # 		print(cls.__name)


# # A.__name
# # A.bar()
# # class B(A):
	
# # 	@classmethod
# # 	def foo(cls):
# # 		print(cls.__name)
# # B.foo()

# # print(bin(13))
# # print(bin(14))
# # print(13 ^ 14)
# # print(bin(3))

# # print(bin(45))
# # print(bin(46))

# from lesson9 import is_palindrome
# # from main import is_palindrome as is_palindrome2
# # from core import User

# # print(is_palindrome('Шалаш'))


from itertools import *

# for i in repeat('hello', 3):  # ['hello', 'hello', 'hello']
# 	print(i)

# print(*product('abcd', 'efgh'))
# print(*takewhile(lambda x: x != 4, [1, 2, 3, 4, 5, 6, 7, 8]))
# print(*dropwhile(lambda x: x != 4, [1, 2, 3, 4, 5, 6, 7, 8]))

# print(*compress([1, 2, 3, 4, 5, 6], [0, 1, 1, 0, 0, 1]))

# for i in chain([1, 2, 3], [4, 5, 6]):
# 	print(i)

# print(*chain.from_iterable([[1, 2, 3], [4, 5, 6]]))

# print(*islice('hello', 0, 5))

# print(*zip_longest('hello', 'pythonworld'))


# print(*accumulate([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent


from datetime import datetime, timedelta

# delta = timedelta(days=5)
# date1 = datetime(2023, 12, 15)
# print(datetime.now() + delta)

# print(datetime.now().timestamp())
# print(datetime.fromtimestamp(1683019104.375687))

# print(datetime.now().strftime("%b, %d %Y, %H:%M"))
# print(datetime.strptime('May, 02 2023, 12:20', "%b, %d %Y, %H:%M"))
# from enum import IntEnum, Enum
# from http import HTTPStatus


# Role = Enum('Role', (('ADMIN', 2), ('MANAGER', 1), ('USER', 3)))
# print(Role.ADMIN.value)
# class Role(IntEnum):
# 	ADMIN = 1
# 	MANAGER = 2
# 	USER = 3


# role_id = 2
# if role_id == Role.MANAGER:
# 	pass
# status_code = 403
# if status_code == 200:
# 	print('OK')


# print(HTTPStatus.FORBIDDEN.value)

# from argparse import ArgumentParser


# parser = ArgumentParser()
# parser.add_argument('--host', help='HOST', default='127.0.0.1')
# parser.add_argument('-d', '--debug', action='store_true', help='DEBUG')
# args = parser.parse_args()
# print(args)

import logging


logging.basicConfig(
	level=logging.INFO,
	format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
	filename='log.log',
	filemode='a'
)


logging.info('First LOG')
logging.error('Error')
try:
	a = 4 / 0
except ZeroDivisionError as e:
	logging.error(e)