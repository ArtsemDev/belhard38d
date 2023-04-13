# # N = 5  # count
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
