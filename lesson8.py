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

