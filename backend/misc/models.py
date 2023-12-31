from pydantic import BaseModel


class UserModel(BaseModel):
    name: str | None = None
    phone: str| None = None
    email: str | None = None
    login: str
    password: str


class ArticleModel(BaseModel):
    title: str
    slug: str
    text: str
    tags: list[str]


class DonatorModel(BaseModel):
    name: str
    url: str
    amount: float


class CookieModel(BaseModel):
    field: dict
