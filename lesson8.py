
from collections import namedtuple


Category = namedtuple('Category', ('id', 'name', 'slug'))
Product = namedtuple('Product', ('id', 'title', 'price'))


def validate_http_params(data: namedtuple):
	def wrapped(func):
		def wrapper(url: str, query: dict[str, str]):
			if not isinstance(url, str):
				raise TypeError('argument url must be string')

			if not isinstance(query, dict):
				raise TypeError('argument query must be dictionary')

			if not url.startswith('http://'):
				if not url.startswith('https://'):
					raise ValueError('invalid URL')

			for key, value in query.items():
				if not isinstance(key, str) or not isinstance(value, str):
					raise ValueError('invalid query params')

			objs = func(url, query)
			return [data(**obj) for obj in objs]

		return wrapper
	return wrapped


@validate_http_params(data=Category)
def get_response(url: str, query: dict[str, str]) -> dict:
	return [
		{
			'id': 1,
			'name': 'Coffee',
			'slug': 'coffee'
		},
		{
			'id': 2,
			'name': 'Tea',
			'slug': 'tea'
		}
	]


@validate_http_params(data=Product)
def get_products(url: str, query: dict[str, str]) -> dict:
	return [
		{
			'id': 5,
			'title': 'Latte',
			'price': 5.5
		}
	]


class User:
	role = 'user'
	
	def __init__(self, first_name, email, age, height, weight):
		self.name = first_name.title()
		self.email = email.lower()
		self.age = age
		self.height = height / 100
		self.weight = weight
		self.city = None
		self.__i = 0

	def dict(self) -> dict:
		return {
			'name': self.name,
			'email': self.email,
			'city': self.city
		}

	@classmethod
	def change_role(cls, value):
		cls.role = value

	def __str__(self):
		return f'User: name={self.name}, email={self.email} city={self.city}'

	def __gt__(self, other):
		if isinstance(other, User):
			self_bmi = self.weight / (self.height ** 2)
			other_bmi = other.weight / (other.height ** 2)
			return self_bmi > other_bmi
		elif isinstance(other, (int, float)):
			self_bmi = self.weight / (self.height ** 2)
			return self_bmi > other
		raise TypeError

	def __ge__(self, other):
		if isinstance(other, User):
			self_bmi = self.weight / (self.height ** 2)
			other_bmi = other.weight / (other.height ** 2)
			return self_bmi >= other_bmi
		elif isinstance(other, (int, float)):
			self_bmi = self.weight / (self.height ** 2)
			return self_bmi >= other
		raise TypeError

	def __lt__(self, other):
		return not self.__ge__(other)

	def __le__(self, other):
		return not self.__gt__(other)

	def __eq__(self, other):
		if isinstance(other, User):
			self_bmi = self.weight / (self.height ** 2)
			other_bmi = other.weight / (other.height ** 2)
			return self_bmi == other_bmi
		elif isinstance(other, (int, float)):
			self_bmi = self.weight / (self.height ** 2)
			return self_bmi == other
		raise TypeError

	def __ne__(self, other):
		return not self.__eq__(other)

	def __add__(self, other):
		if isinstance(other, User):
			return self.age + other.age
		elif isinstance(other, (int, float)):
			return self.age + other
		raise TypeError

	def __radd__(self, other):
		return self.__add__(other)

	def __iter__(self):
		return self

	def __next__(self):
		if self.__i < self.age:
			self.__i += 1
			return self.__i
		raise StopIteration

	def __len__(self):
		return round(self.height * 100)

# TODO Написать класс Category
#  1. Объявить атрибут класса objs: list
#  2. Написать метод класса add, принимающий строку(
#  название новой категории), метод должен проверять, что такой
#  категории нет в списке objs, в противном случае вызывать исключение
#  ValueError, если же название уникальное, то добавлять в список
#  и возвращать его индекс в списке

class Category:
	objs: list = []

	@classmethod
	def add(cls, name: str) -> int:
		if name.title() in cls.objs:
			raise ValueError('category name is not unique')
		cls.objs.append(name.title())
		return cls.objs.index(name.title())


# TODO Написать класс Numbers
#  1. Конструктор класса принимает список чисел и объявляет 
#  атрибут объекта на его основании
#  2. Написать метод average возвращающий среднее арифмитическое 
#  чисел
#  3. Написать метод most_common возвращающий число из списка
#  которое встречается чаще всего, если таких чисел несколько
#  то вернуть среднее между ними

class Numbers:

	def __init__(self, *numbers):
		self.numbers = numbers

	def average(self) -> float:
		return sum(self.numbers) / len(self.numbers)

	def most_common(self):
		most_common_number = max(self.numbers, key=self.numbers.count)
		count = self.numbers.count(most_common_number)
		objs = [*filter(lambda x: self.numbers.count(x) == count, self.numbers)]
		return sum(objs) / len(objs)


# TODO Написать класс Rectangle
#  1. конструктор класса принимает координаты точек прямоугольника
#  по диагонали
#  2. Написать метод объекта perimeter возвращающий периметр
#  данного прямоугольника
#  3. написать метод объекта square возвращающий площадь 
#  данного прямоугольника

class Rectangle:

	def __init__(self, x1, y1, x2, y2):
		self.height = abs(x1 - x2)
		self.width = abs(y1 - y2)

	def perimeter(self):
		return 2 * (self.height + self.width)

	def square(self):
		return self.height * self.width


def decorator(func):
	pass
# 	print(func)
# 	def wrapper(*args, **kw):
# 		return func(*args, **kw)

# 	return wrapper


# @decorator
# def multiply(a, b):
# 	return a * b


# @decorator
# def foo():
# 	print('foo')

class Dispatcher:

	handlers: dict = {}

	def __call__(self, button):
		def decorator(func):
			self.handlers[button] = func
			def wrapper(*args, **kw):
				return func(*args, **kw)

			return wrapper
		return decorator

	def start(self, button, *args, **kw):
		if button in self.handlers:
			self.handlers[button](*args, **kw)


dp = Dispatcher()


@dp('A')
def foo():
	print('foo')


@dp('B')
def bar():
	print('bar')


button = 'B'
dp.start(button)
