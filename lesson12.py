from csv import DictReader, DictWriter

from pydantic import BaseModel, Field
from pydantic.types import Decimal


class Product(BaseModel):
	title: str = Field(max_length=64)
	description: str = Field(default=None)
	price: Decimal = Field(max_digits=8, decimal_places=2)


	@classmethod
	def from_csv(cls, path: str, encoding: str = 'utf-8') -> list["Product"]:
		with open(path, 'r', encoding=encoding) as file:
			reader = DictReader(file)
			return [cls(**data) for data in reader]

	@classmethod
	def to_csv(cls, products: list["Product"], path: str, mode: str = 'w', encoding: str = 'utf-8') -> None:
		with open(path, mode, encoding=encoding) as file:
			writer = DictWriter(file, products[0].dict().keys())
			if mode == 'w':
				writer.writeheader()
			writer.writerows([product.dict() for product in products])


class MyStr(str):

	def all_strip(self, symbols: str) -> str:
		return ''.join([symbol for symbol in self if symbol not in symbols])



from sqlite3 import connect


conn = connect('db.sqlite3')  # .db .sqlite3
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS category(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(64) NOT NULL UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS product(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(64) NOT NULL UNIQUE,
	description TEXT,
	price DECIMAL(8, 2) NOT NULL DEFAULT(100.0),
	category_id INTEGER NOT NULL,
	FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
);
''')
conn.commit()


# cur.executemany('''
# 	INSERT INTO category(name) VALUES(?);
# ''', (('Coffee', ), ('Tea', )))
# conn.commit()

# cur.executemany('''
# INSERT INTO product(title, description, price, category_id)
# VALUES(?, ?, ?, ?);
# ''', (('Capuchino', 'With Milk', 5, 1), ('Пуэр', '12 years', 35.45, 2)))
# conn.commit()

# cur.execute('''
# UPDATE category SET name = ? WHERE id = ?;
# ''', ('Кофе', 3))
# conn.commit()

# cur.execute('''
# DELETE FROM category WHERE id = ?;
# ''', (4, ))
# conn.commit()


# cur.execute('''
# SELECT * FROM product WHERE price > ? ORDER BY title;
# ''', (1, ))
# print(cur.fetchall())


# cur.execute('''
# SELECT category.name, product.title, product.price
# FROM category
# JOIN product
# ON product.category_id = category.id;
# ''')
# print(cur.fetchall())


from psycopg2 import connect


conn = connect('postgresql://belhard:belhard@localhost:5432/bh38d')

with conn.cursor() as cur:
	# cur.execute('''
	# 	CREATE TABLE IF NOT EXISTS category(
	# 		id SERIAL PRIMARY KEY,
	# 		name VARCHAR(64) NOT NULL UNIQUE
	# 	);
	# ''')
	# conn.commit()
	# cur.execute('''
	# 	INSERT INTO category(name) VALUES(%s);
	# ''', ('Coffee', ))
	# conn.commit()
	cur.execute('SELECT * FROM category;')
	print(cur.fetchall())
