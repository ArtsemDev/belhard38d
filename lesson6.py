# N = 5  # count
# # M = 13  # division
# # K = 100  # start


# # while N:
# # 	if not K % M:
# # 		print(K)
# # 		N -= 1
# # 		K += M
# # 	else:
# # 		K += 1


# N = 44
# # c = 0
# # for i in range(2, N+1, 2):
# # 	print(i, end=' ')
# # 	c += 1
# # 	if c == 5:
# # 		c = 0
# # 		print()

# for i in range(2, N+1, 10):
# 	for j in range(i, i+9, 2):
# 		if j > N:
# 			break
# 		print(j, end=' ')
# 	print()


# FIFO
# LIFO
# objs = []
# for i in range(10):
# 	objs.append(i)
# 	print(objs)

# while objs:
# 	del objs[0]
# 	print(objs)


# def multiply(numbers):
# 	res = 1
# 	for number in numbers:
# 		res *= number
# 	print(res)


# multiply([1, 2, 3, 4, 5])


# def foo(a, b=5):
# 	print(a * b)


# foo(4, 3)


# def bar(a, b=None):
# 	if b is None:
# 		b = []
# 	b.append(a)
# 	print(b)


# bar(4)
# bar(4)


# def baz(*args):
# 	print(args)


# baz(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


# def foo(**kwargs):
# 	print(kwargs)

# foo(a=6, b=7, name='alex')



# def foo(a, b, *args, c=5, d=None):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print(d)
# 	print(args)


# foo(1, 2, 3, 4, 5, 6, a=7, b=8, c=9, d=0)


# def multiply(*numbers):
# 	res = 1
# 	for number in numbers:
# 		res *= number
# 	return res


# objs = [1, 2, 3, 4, 5]
# a = multiply(*objs)
# print(a)


# def foo(a, b):
# 	print(a, b)


# data = {
# 	'a': 5,
# 	'b': 4
# }

# foo(**data)


# def bar(a, b, c, d, e=8):
# 	print(a, b, c, d, e)


# objs = [1, 2, 3, 4, 5]
# bar(*objs)



# objs = [1, 2, 3, 4, 5, 6]
# a, b, c, *_ = objs
# print(a, b, c, _)


# numbers = [i for i in range(1, 101)]
# numbers = [*range(1, 101)]


# objs1 = [1, 2, 3, 4]
# objs2 = [5, 6, 7, 8]
# objs3 = [*objs1, *objs2]
# print(objs3)


# for _ in range(5):
# 	print('Hello')


# def foo():
# 	return 2, 3, 4, 5

# a, b, c, d = foo()
# print(a, b, c, d)


# TODO Написать функцию (average), принимающая неопределенное
#  колличество аргументов (чисел)
#  и возвращающая среднее арифметическое


# def average(*args):
# 	return sum(args) / len(args)


# print(average(1, 2, 3, 4, 5))
# LEGB - Local Enclosing Global Builtin
# a = 5

# def foo():
# 	a = 4

# 	def bar():
# 		nonlocal a
# 		print(a)

# 	print(locals())
	# for _ in range(10):
	# 	bar()


# print(foo())
# print(globals().get('foo')())


# def foo(a):
# 	def bar(b):
# 		return a * b

# 	return bar


# res = foo(5)
# res2 = foo(8)
# print(res(4))
# print(res(3))
# print(res(5))
# print(res2(4))
# print(res2(3))
# print(res2(5))

# data = [f'user{i}' for i in range(100)]


# def get_users():
# 	for user in data:
# 		yield user


# for user in get_users():
# 	print(user)
# res = get_users()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


def foo():
	a = 0
	b = 7

	# if a:
	# 	return a
	# else:
	# 	return b
	# return a if a else b

	# return a and b  - a если а True иначе b
	# return a or b  - b если а True иначе a


# objs = [2, 3, 2, 5, 4, 7, 4, 6, 5, [6, 4, 5, 3, 5, 2, [8, 6, 7, 5, 6, ], [6, 4, 5, 3, 2, 4, 3, ], 7, 6, 4, 5, 3, [8, 6, 7, 4, 6, 3, [6, 2, 4, 2, 4, 2, [7, 5, 7, 4, 6, [6, 4, 5, 3, 1, 4]]]]]]


# def recursive_multiply(numbers):
# 	res = 1
# 	for number in numbers:
# 		if isinstance(number, (int, float)):
# 			res *= number
# 		else:
# 			res *= recursive_multiply(number)
# 	return res


# print(recursive_multiply(objs))


# multiply = lambda x, y: x * y
# print(multiply(4, 5))


# objs = ['age', 'python', 2, 'pycharm', 3, 4, 'hello', 'world']
# # ['2', '3', '4', 'hello', 'world']
# objs.sort(key=lambda x: str(x) if not isinstance(x, str) else x)
# print(objs)

# words = ['Hello', 'python', 'age', 'apple', 'Windows']
# words.sort(key=lambda x: x.lower())
# print(words)


# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# list comprehension
# result = [int(x) ** 2 for x in numbers]
# map
# result = [*map(lambda x: int(x) ** 2, numbers)]
# print(result)
# for
# result = []
# for x in numbers:
# 	result.append(int(x) ** 2)


# objs = ['hello', 3, 4, 3, 'world', [3, 4, 5], 'python']
# list comprehension
# result = [obj for obj in objs if isinstance(obj, str)]
# print(result)
# for
# result = []
# for obj in objs:
# 	if isinstance(obj, str):
# 		result.append(obj)
# filter
# result = [*filter(lambda x: isinstance(x, str), objs)]
# print(result)


# text = 'hello'
# number = [2, 3, 4, 5]
# objs = (True, False, None)

# result = [*zip(text, number, objs)]
# print(result)
# from itertools import zip_longest



# numbers = iter(range(2, 45, 2))
# result = [[*filter(lambda x: x, line)] for line in zip_longest(numbers, numbers, numbers, numbers, numbers)]
# for line in result:
# 	print(*line)
