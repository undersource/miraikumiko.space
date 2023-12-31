from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from base64 import b64encode
from backend.misc.database import session
from backend.misc.database import User, Article, Tag, Donator
from backend.misc.database import get_article_tags_id, get_articles_of_tag
from backend.misc.models import UserModel, ArticleModel, CookieModel
from backend.misc.security import verify_password

app = FastAPI()
security = HTTPBasic()


@app.get("/api/articles")
async def get_articles():
    articles = session.query(Article).all()

    return articles


@app.get("/api/tags")
async def get_tags():
    tags = session.query(Tag).all()

    return tags


@app.get("/api/donators")
async def get_donators():
    donators = session.query(Donator).all()

    return donators


@app.get("/api/article/{slug}")
async def get_article(slug: str):
    article = session.query(Article).filter(Article.slug.in_((slug,))).first()

    return article


@app.get("/api/article/{id}/tags")
async def get_article_tags(id: int):
    tags = []
    article_tags_id = get_article_tags_id(id)

    for tag_id in article_tags_id:
        tag = session.query(Tag).filter(Tag.id.in_((tag_id[1],))).first()
        tags.append(tag)

    return tags


@app.get("/api/tag/{name}")
async def get_tag(name: str):
    tag = session.query(Tag).filter(Tag.name.in_((name,))).first()

    return tag


@app.get("/api/tag/{name}/articles")
async def get_tag_articles(name: str):
    articles = get_articles_of_tag(name)

    return articles


@app.post("/api/article/post")
async def post_article(data: ArticleModel, credentials: HTTPBasicCredentials = Depends(security)):
    login = credentials.username
    password = credentials.password
    query = session.query(User).filter(User.login.in_((login,))).first()

    if query is not None:
        if not verify_password(password, query.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    article = Article()

    query = session.query(Article).filter(Article.title.in_((data.title,))).first()

    if query is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Title already exist")

    query = session.query(Article).filter(Article.slug.in_((data.slug,))).first()

    if query is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Slug already exist")
    
    article.title = data.title
    article.slug = data.slug
    article.text = data.text

    for name in data.tags:
        tag = session.query(Tag).filter(Tag.name.in_((name,))).first()

        if tag is None:
            tag = Tag(name=name)

        article.tags.append(tag)
            
    session.add(article)
    session.commit()

    return status.HTTP_200_OK


@app.get("/api/auth")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    login = credentials.username
    password = credentials.password
    query = session.query(User).filter(User.login.in_((login,))).first()

    if query is not None:
        if not verify_password(password, query.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    token = b64encode(f"{login}:{password}".encode('utf-8'))

    return { "token": token }


@app.get("/api/dashboard")
async def dashboard(cookie: CookieModel):
    return
