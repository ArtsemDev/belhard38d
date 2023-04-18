# Task 6_1
def decimal_to_binary(decimal: int) -> str:
	binary: str = ''
	while decimal > 1:
		binary = f'{decimal % 2}' + binary
		decimal //= 2
	binary = f'{decimal}' + binary
	return binary


def binary_to_decimal(binary: str) -> int:
	binary = binary[::-1]
	decimal: int = 0
	for i in range(len(binary)):
		decimal += (2 ** i) * int(binary[i])
	return decimal

# Task 6_2
def encode_morse(text: str) -> str:
	morses_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": " ",
    }

	morse: str = ''
	for el in text.upper():
		if el in morses_code:
			morse += morses_code[el] + ' '
	return morse


def decode_morse(morse: str) -> str:
	morses_code = {
		'.-': 'A', 
		'-...': 'B', 
		'-.-.': 'C', 
		'-..': 'D', 
		'.': 'E', 
		'..-.': 'F', 
		'--.': 'G', 
		'....': 'H', 
		'..': 'I', 
		'.---': 'J', 
		'-.-': 'K', 
		'.-..': 'L', 
		'--': 'M', 
		'-.': 'N', 
		'---': 'O', 
		'.--.': 'P', 
		'--.-': 'Q', 
		'.-.': 'R', 
		'...': 'S', 
		'-': 'T', 
		'..-': 'U', 
		'...-': 'V', 
		'.--': 'W', 
		'-..-': 'X', 
		'-.--': 'Y', 
		'--..': 'Z', 
		'-----': '0', 
		'.----': '1', 
		'..---': '2', 
		'...--': '3', 
		'....-': '4', 
		'.....': '5', 
		'-....': '6', 
		'--...': '7', 
		'---..': '8', 
		'----.': '9', 
		'|': ' '
	}
	morse = morse.replace('   ', ' | ')
	text: str = ''
	for el in morse.split():
		if el in morses_code:
			text += morses_code[el]
	return text


# Task 6_3
def slice_list(objs: list, offset: int) -> list:
	if abs(offset) >= len(objs):
		offset -= (offset // len(objs)) * len(objs)
	return objs[-offset:] + objs[:-offset]


# Task 6_4
objs = [1, 2, 3, 'wer', 'qwe', 4, 5, True, 'asdf']
# objs = [obj for obj in objs if isinstance(obj, str)]
# objs = [*filter(lambda x: isinstance(x, str), objs)]
# for i in range(len(objs)):
# 	if not isinstance(objs[i], str):
# 		del objs[i]

# for obj in objs:
# 	if not isinstance(obj, str):
# 		objs.remove(obj)

# i = 0
# while i < len(objs):
# 	if not isinstance(objs[i], str):
# 		del objs[i]
# 	else:
# 		i += 1

# for i in range(len(objs) - 1, -1, -1):
# 	if not isinstance(objs[i], str):
# 		del objs[i]
# print(objs)

# Task 6_5
def reverse(objs: list) -> list:
	for i in range(0, len(objs) // 2):
		objs[i], objs[~i] = objs[~i], objs[i]
	return objs


# Task 6_6
# odd: list = []
# even: list = []
# for number in numbers:
# 	if number % 2:
# 		odd.append(number)
# 	else:
# 		even.append(number)
# result = even + odd
# print(result)
def even_odd_sort(numbers: list[int | float]) -> list[int | float]: 
	j = 0
	for i in range(len(numbers)):
		if not numbers[i] % 2:
			numbers.insert(j, numbers.pop(i))
			j += 1
	return numbers


# Task 6_7
numbers = [1, 2, 3, 4, 5]
# result = []
# for i in range(len(numbers)):
# 	if i != len(numbers) - 1:
# 		result.append(numbers[i-1] + numbers[i+1])
# 	else:
# 		result.append(numbers[i-1] + numbers[0])
# print(result)

def sum_of_neighbors(numbers: list[int | float]) -> list[int | float]:
	return [(numbers[i-1] + numbers[i+1]) if i != len(numbers) - 1 else (numbers[i-1] + numbers[0]) for i in range(len(numbers))]


# Task 6_8
def find_country(city: str) -> str:
	countries = {
		'Belarus': ['Minsk', 'Gomel', 'Mogilev'],
		'Russian': ['Moscow', 'SPB', 'Kaliningrad']
	}
	for country, cities in countries.items():
		if city in cities:
			return country


# Task 6_9
users = {
	1: {
		'name': 'Alex',
		'email': 'alex@gmail.com'
	},
	2: {
		'name': 'Pavel',
		'email': ''
	},
	3: {
		'name': 'Masha'
	},
	4: {
		'name': 'Maksim',
		'email': None
	}
}
for user in users.values():
	if not user.get('email'):
	# if 'email' not in user or user['email'] == '' or user['email'] if None:
		print(user.get('name'))
