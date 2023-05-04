# from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent


# # file = open(BASE_DIR / 'input.txt', 'r', encoding='utf-8')
# # print(file.read())
# # print(file.readline())
# # print(file.readline())
# # print(file.readlines())
# # lines = [line.strip() for line in file if line.strip()]
# # file.seek(0)
# # print(file.read())
# # file.close()

# # file = open('output.txt', 'w', encoding='utf-8')
# # file.writelines(['hello\n', 'python\n', 'world'])
# # file.close()


# # with (
# # 	open('input.txt', 'r', encoding='utf-8') as file_in,
# # 	open('output.txt', 'w', encoding='utf-8') as file_out
# # ):
# # 	print(file_in.read())

# # print('file closed!')


# # TODO Дан многострочный файл, необходимо считать файл
# #  для каждой строки в файле подсчитать колличество слов
# #  и колличество букв, результат записать в новый файл в формате
# #  Строка 1: 2 слова 10 букв
# #  ...
# # with (
# # 	open('input.txt', 'r', encoding='utf-8') as file_in,
# # 	open('output.txt', 'w', encoding='utf-8') as file_out
# # ):
# # 	lines = []
# # 	c = 1
# # 	for line in file_in:
# # 		line = line.strip()
# # 		word_count = line.count(' ') + 1 if line else 0
# # 		letter_count = len([i for i in line if i.isalpha()])
# # 		lines.append(f'Строка {c}: {word_count} слов {letter_count} букв\n')
# # 		c += 1
# # 	file_out.writelines(lines)
# try:
# 	import ujson as json
# except ModuleNotFoundError:
# 	import json
# # with open('input.json', 'r', encoding='utf-8') as file:
# # 	data = load(file)
# # print(data)

# user = {
# 	'name': 'Алекс',
# 	'is_human': True
# }

# with open('output.json', 'w', encoding='utf-8') as file:
# 	json.dump(user, file, indent=2, ensure_ascii=False)


from pydantic import BaseModel


class User(BaseModel):
	username = 

