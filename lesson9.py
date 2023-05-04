# # class Car:

# # 	def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
# # 		self.color = color
# # 		self.count_passenger_seats = count_passenger_seats
# # 		self.is_baby_seat = is_baby_seat
# # 		self.is_busy = False

# # 	def __str__(self):
# # 		return self.color

# # 	def __bool__(self):
# # 		return self.is_busy


# # class Taxi:

# # 	def __init__(self, cars: list[Car]):
# # 		self.cars = cars

# # 	def find_car(self, count_passenger: int, is_baby: bool):
# # 		cars = filter(lambda x: not x.is_busy, self.cars)
# # 		if is_baby:
# # 			cars = filter(lambda x: x.is_baby, cars)
		
# # 		for car in cars:
# # 			if car.count_passenger_seats >= count_passenger:
# # 				car.is_busy = True
# # 				return car


# # class Category:
# # 	categories: list[dict] = []

# # 	@classmethod
# # 	def add(cls, name: str) -> int:
# # 		for category in cls.categories:
# # 			if category.get('name') == name.title():
# # 				raise ValueError('category is not unique')

# # 		cls.categories.append(
# # 			{
# # 				'name': name.title(),
# # 				'is_published': False
# # 			}
# # 		)
# # 		return len(cls.categories) - 1

# # 	@classmethod
# # 	def get(cls, index: int) -> dict:
# # 		return cls.categories[index]

# # 	@classmethod
# # 	def delete(cls, index: int) -> None:
# # 		try:
# # 			del cls.categories[index]
# # 		except IndexError:
# # 			pass

# # 	@classmethod
# # 	def update(cls, index: int, name: str):
# # 		try:
# # 			obj = cls.get(index)
# # 		except IndexError:
# # 			return cls.add(name)
# # 		else:
# # 			for category in cls.categories:
# # 				if category.get('name') == name.title():
# # 					raise ValueError('category is not unique')
# # 			obj['name'] = name.title()

# # 	@classmethod
# # 	def make_published(cls, index: int):
# # 		obj = cls.get(index)
# # 		obj['is_published'] = True


# # 	@classmethod
# # 	def make_unpublished(cls, index: int):
# # 		obj = cls.get(index)
# # 		obj['is_published'] = False	


# # class User:

# # 	def __init__(self, name: str, email: str) -> None:
# # 		self.name = name.title().strip()
# # 		self.email = email.lower().strip()
# # 		self.is_active = True

# # 	def __str__(self) -> str:
# # 		# return f'User (name={self.name}, email={self.email})'
# # 		return self.email

# # 	def __bool__(self) -> bool:
# # 		return self.is_active


# # class Admin(User):

# # 	def __init__(self, name: str, email: str, salary: float):
# # 		super().__init__(name, email)
# # 		self.salary = salary

# # 	def __str__(self):
# # 		return self.name

# # 	def dict(self):
# # 		return {
# # 			'name': self.name,
# # 			'email': self.email,
# # 			'is_active': self.is_active,
# # 			'salary': self.salary
# # 		}



# # class A(object):
# # 	name = 'A'


# # class B(A):
# # 	name = 'B'


# # class C(A):
# # 	name = 'C'


# # class D(C, B):
# # 	pass


# # class Cat:

# # 	@classmethod
# # 	def say(cls):
# # 		print('meow')


# # class Dog:

# # 	@classmethod
# # 	def say(cls):
# # 		print('woof')


# # def say(obj: Cat | Dog):
# # 	# if isinstnace(obj, Cat):
# # 	# 	obj.say_meow()
# # 	# elif isinstance(obj, Dog);
# # 	# 	obj.say_woof()
# # 	obj.say()


# # class DebitCard:

# # 	def __init__(self, number: str):
# # 		self.__card_number = number

# # 	@property
# # 	def card_number(self):
# # 		return self.__card_number[:6] + '*'*10 + self.__card_number[-4:]

# # 	@card_number.setter
# # 	def card_number(self, value):
# # 		if not isinstance(value, str):
# # 			raise TypeError

# # 		if len(value) != 16:
# # 			raise ValueError

# # 		if not value.isdigit():
# # 			raise ValueError

# # 		self.__card_number = value


# # class Person:

# # 	def __init__(self, name, surname):
# # 		self.name = name
# # 		self.surname = surname

# # 	@property
# # 	def full_name(self):
# # 		return f'{self.name} {self.surname}'


# # class Engine:

# # 	def __init__(self, volume):
# # 		self.volume = volume


# # class Car:

# # 	def __init__(self, name: str, color: str, engine: Engine):
# # 		self.name = name
# # 		self.color = color
# # 		self.engine = engine


# # class Manufactory:

# # 	@classmethod
# # 	def create_bmw(cls, count):
# # 		objs = []
# # 		for i in range(count):
# # 			car = Car('name', 'color', 'engine')
# # 			objs.append(car)
# # 		return objs


# # from abc import ABC, abstractmethod


# # class Model(ABC):

# # 	@classmethod
# # 	@abstractmethod
# # 	def add(cls, name: str) -> int:
# # 		pass

# # 	@classmethod
# # 	@abstractmethod
# # 	def get(cls, index: int) -> dict:
# # 		pass

# # 	@classmethod
# # 	def delete(cls, index):
# # 		pass


# # class Product(Model):
	
# # 	@classmethod
# # 	def add(cls, name: str):
# # 		pass

# # 	@classmethod
# # 	def get(cls, index: int):
# # 		pass


# # class CallFunction(ABC):

# # 	@abstractmethod
# # 	def call(self):
# # 		pass


# # class InternetFunction(ABC):

# # 	@abstractmethod
# # 	def internet(self):
# # 		pass


# # class SMSFunction(ABC):

# # 	@abstractmethod
# # 	def sms(self):
# # 		pass


# # class MobilePhone(CallFunction, InternetFunction, SMSFunction):

# # 	def call(self):
# # 		pass

# # 	def internet(self):
# # 		pass

# # 	def sms(self):
# # 		pass


# # class Phone(CallFunction):

# # 	def call(self):
# # 		pass


# # from dataclasses import dataclass


# # @dataclass
# # class User:
# # 	name: str
# # 	email: str
# # 	age: int


# # # vasya = User(name='vasya', email='vasya@gmail.com', age=35)
# # # print(vasya.email)
# # # vasya.email = 'petrov@gmail.com'
# # # print(vasya.email)


# # # class A(type):
# # # 	pass

# def __init__(self, name, email):
# 	self.name = name
# 	self.email = email


# # User = type('User', (), {'name': None, 'email': None, '__init__': __init__})
# # vasya = User(name='vasya', email='vasya@gmail.com')
# # print(vasya.email)


# # class A:

# # 	def __call__(self):
# # 		print('call')

# # a = A()
# # a()

# # Kiss
# # Yagni


# # TODO Написать класс DictReader
# #  конструктор класса принимает список строк в формате:
# #  [
# # 		'name,email,age', 
# # 		'vasya,vasya@gmail.com,35', 
# # 		'petya,petya@mail.com,24'
# #  ]
# #  Написать метод объекта read возвращающий список словарей:
# #  [
# #  	{'name': 'vasya', 'email': 'vasya@gmail.com', 'age': '35'},
# #  	{'name': 'petya', 'email': 'petya@mail.com', 'age': '24'}
# #  ]

# class DictReader:

# 	def __init__(self, data: list[str]) -> None:
# 		self.data = data

# 	def read(self) -> list[dict]:
# 		keys = self.data[0].split(',')  # ['name', 'email', 'age']
# 		values = map(lambda x: x.split(','), self.data[1:])  # [['vasya', 'vasya@gmail.com', '35'], ['petya', 'petya@mail.com', '24']]
# 		return [dict(zip(keys, value)) for value in values]

# r = DictReader([
# 		'name,email,age', 
# 		'vasya,vasya@gmail.com,35', 
# 		'petya,petya@mail.com,24'
#  ])
# print(r.read())


def is_palindrome(text: str) -> bool:
	return text.lower() == text.lower()[::-1]


if __name__ == '__main__':
	print(is_palindrome('text'))
