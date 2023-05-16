# from csv import reader, DictWriter
#
# from psycopg2 import connect
# from psycopg2.extras import NamedTupleCursor
#
#
# conn = connect('postgresql://belhard:belhard@localhost:5432/bh38d')
#
#
# # with (
# #     open('category.csv', 'r', encoding='utf-8') as file,
# #     conn.cursor() as cur
# # ):
# #     r = reader(file)
# #     cur.executemany('''
# #         INSERT INTO category(name) VALUES(%s);
# #     ''', [(name[0], ) for name in r if name[0] != 'name'])
# #     conn.commit()
#
# with (
#     open('category_out.csv', 'w', encoding='utf-8') as file,
#     conn.cursor(cursor_factory=NamedTupleCursor) as cur
# ):
#     cur.execute('''select * from category;''')
#     w = DictWriter(file, fieldnames=('id', 'name'))
#     w.writeheader()
#     w.writerows([category._asdict()for category in cur.fetchall()])

from sqlalchemy import Column, SMALLINT, VARCHAR, INT, ForeignKey, DECIMAL, create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://belhard:belhard@localhost:5432/bh38d')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls) -> str:
        return ''.join([f'_{i.lower()}' if i.isupper() else i for i in cls.__name__]).strip('_')


class Category(Base):
    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(64), unique=True, nullable=False)


class Product(Base):
    title = Column(VARCHAR(64), nullable=False)
    description = Column(VARCHAR(2048))
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(SMALLINT, ForeignKey(Category.id, ondelete='CASCADE'), nullable=False)

    @property
    def category(self) -> Category:
        with self.session() as session:  # type: Session
            obj = session.get(Category, self.category_id)
            return obj


class User(Base):
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)


# with Base.session() as session:  # type: Session
#     categories = [
#         Category(name='Кофе'),
#         Category(name='Cэндвичи'),
#     ]
#     #  add записываю 1 объект
#     #  add_all записываю много объектов
#     session.add_all(categories)
#     session.commit()
#     for category in categories:
#         session.refresh(category)
#         print(category.id, category.name)

from sqlalchemy import update, select, delete


# with Base.session() as session:  # type: Session
#     session.execute(
#         update(Category)
#         .values(name='Coffee')
#         # .filter_by(id=1)
#         .filter(Category.id == 1)
#     )
#     session.commit()

# with Base.session() as session:  # type: Session
#     # categories = session.scalars(
#     #     select(Category)
#     #     .order_by(Category.id.desc())
#     # )
#     # print(categories.all())
#     objs = session.execute(
#         select(Category, Product)
#         .join(Product)
#     )
#     print(*objs)


# with Base.session() as session:  # type: Session
#     product = Product(
#         title='Эспрессо',
#         description='Робуста',
#         price=4,
#         category_id=1
#     )
#     session.add(product)
#     session.commit()
#     session.refresh(product)


from pydantic import BaseModel, Field
from pydantic.types import Decimal


class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    category_id: int
    price: Decimal = Field(max_digits=8, decimal_places=2)

    class Config:
        orm_mode = True


with Base.session() as session:  # type: Session
    product = session.get(Product, 1)

# schema = ProductSchema(**product.__dict__)
schema = ProductSchema.from_orm(product)

# print(product.__dict__)
# with Base.session() as session:  # type: Session
#     product.title = 'Cappuccino'
#     session.add(product)
#     session.commit()
