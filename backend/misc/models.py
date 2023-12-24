from pydantic import BaseModel
from collections.abc import Mapping


class UserModel(BaseModel):
    name: str
    password: str


class ArticleModel(BaseModel):
    title: str
    slug: str
    text: str
    tags: list[str]


class PostArticleData(BaseModel):
    data: Mapping[str, UserModel | ArticleModel]
