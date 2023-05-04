# from typing import Dict, Any
#
# from pydantic import BaseModel, EmailStr, Field, validator, root_validator
# from pydantic.validators import strict_str_validator
# from phonenumbers import parse, format_number, PhoneNumberFormat
# from phonenumbers.phonenumberutil import NumberParseException
#
#
# db = ['alex@gmail.com', 'vasya@info.com']
#
#
# class PhoneNumberStr(str):
#
#     @classmethod
#     def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
#         field_schema.update(type='string', format='tel')
#
#     @classmethod
#     def __get_validators__(cls):
#         yield strict_str_validator
#         yield cls.validate
#
#     @classmethod
#     def validate(cls, v):
#         try:
#             phone_number = parse(v)
#         except NumberParseException:
#             raise ValueError('invalid phone number format')
#         else:
#             return cls(format_number(phone_number, PhoneNumberFormat.E164))
#
#
# class User(BaseModel):
#     username: str = Field(min_length=4, title='Имя пользователя')
#     email: EmailStr
#     password: str = Field(min_length=8, max_length=64)
#     phone_number: PhoneNumberStr
#     referral: "User" = None
#     languages: list[int]
#
#     @validator('email', pre=True)
#     def validate_email(cls, value):
#         value = value.lower()
#         if value in db:
#             raise ValueError('email is not unique')
#         return value
#
#     @root_validator(pre=True)
#     def validator(cls, values: dict):
#         if values.get('username').lower() in values.get('password').lower():
#             raise ValueError('пароль не должен содержать имя пользователя')
#         return values
#
#     class Config:
#         title = 'Пользователь'
#         description = 'Представление пользователя'
#
#
# User.update_forward_refs()
#
# data = {
#     'username': 'ALEX',
#     'email': 'aaaaaa@gmail.com',
#     'password': 'qwertyui3000',
#     'phone_number': '+375259145208'
# }
# user = User(
#     username='Alex',
#     email='alex@fff.com',
#     password='wertyuiop',
#     phone_number='+375(22)123-45-67',
#     languages=[2, 3, 4, '4', '4.48']
# )
# print(user.dict())
#
# # print(user.schema())

from csv import reader, writer, DictReader, DictWriter

# with open('users.csv', 'r', encoding='utf-8') as file:
#     r = DictReader(file)
#     for i in r:
#         print(i)


users = [
    {'name': 'alex', 'age': 35},
    {'name': 'pavel', 'age': 45},
]

with open('users_out.csv', 'w', encoding='utf-8') as file:
    w = DictWriter(file, fieldnames=('name', 'age'))
    w.writeheader()
    w.writerows(users)


# TODO Написать произвольную простую (без вложенностей) схему Pydatic
#  1. Написать класс метод from_csv принимающий объект file (csv), и возвращающий список
#  экземпляров схемы заполненных на основании этого файла
#  2. Написать метод объекта to_csv принимающий объект файла (сsv) и дозаписывающий\записывающий информацию
#  из схемы в этот сsv файл