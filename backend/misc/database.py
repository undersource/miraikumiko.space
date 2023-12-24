from sqlalchemy import create_engine, Table, Column
from sqlalchemy import Integer, Boolean, Text, DECIMAL, Date, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from sqlalchemy.sql import func, text
from backend.misc.config import config
from backend.misc.logger import logger

DB_TYPE = config["database"]["TYPE"]
DB_HOST = config["database"]["HOST"]
DB_PORT = config["database"]["PORT"]
DB_DATABASE = config["database"]["DATABASE"]
DB_USERNAME = config["database"]["USERNAME"]
DB_PASSWORD = config["database"]["PASSWORD"]

if DB_TYPE == "sqlite":
    DATABASE_URL = f"{DB_TYPE}:///{DB_DATABASE}"
elif DB_TYPE == "mariadb":
    DATABASE_URL = f"{DB_TYPE}+mariadbconnector://{DB_USERNAME}:{DB_PASSWORD}\
    @{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
elif DB_TYPE == "postgresql":
    DATABASE_URL = f"{DB_TYPE}+psycopg2://{DB_USERNAME}:{DB_PASSWORD}\
    @{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
else:
    logger.critical("Unsupported database type \"{DB_TYPE}\"")
    exit(1)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", Text, nullable=False, unique=True, index=True) 
    password = Column("password", Text, nullable=False) 


article_tags = Table(
    "article_tags",
    Base.metadata,
    Column("article_id", Integer, ForeignKey('articles.id')),
    Column("tag_id", Integer, ForeignKey('tags.id'))
)


class Tag(Base):
    __tablename__ = "tags"

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", Text, nullable=False, unique=True, index=True) 


class Article(Base):
    __tablename__ = "articles"

    id = Column("id", Integer, primary_key=True, index=True)
    title = Column("title", Text, nullable=False, unique=True, index=True)
    slug = Column("slug", Text, nullable=False, unique=True, index=True)
    text = Column("text", Text)
    date = Column("date", Date, default=func.current_date())
    tags = relationship("Tag", secondary=article_tags, backref="articles")


class Product(Base):
    __tablename__ = "products"

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", Text, nullable=False, unique=True, index=True)
    description = Column("description", Text)
    price = Column("price", DECIMAL(precision=12, scale=12), nullable=False)
    picture_path = Column("picture_path", Text)


engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)
logger.debug("Tables has been created")

Session = sessionmaker(bind=engine)
session = Session()


def get_article_tags_id(id: int):
    article_tags_id = session.execute(text("SELECT * FROM article_tags WHERE article_id = {id};".format(id=id)))

    return [row for row in article_tags_id]
