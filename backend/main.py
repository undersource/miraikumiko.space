from fastapi import FastAPI
from backend.misc.database import session
from backend.misc.database import User, Article, Tag, get_article_tags_id
from backend.misc.models import PostArticleData
from backend.misc.security import verify_password

app = FastAPI()


@app.get("/api/articles")
async def get_articles():
    articles = session.query(Article).all()

    return articles


@app.get("/api/tags")
async def get_tags():
    tags = session.query(Tag).all()

    return tags


@app.get("/api/article/{slug}")
async def get_article(slug):
    article = session.query(Article).filter(Article.slug.in_((slug,))).first()

    return article


@app.get("/api/article/tags/{id}")
async def get_article_tags(id: int):
    tags = []
    article_tags_id = get_article_tags_id(id)

    for tag_id in article_tags_id:
        tag = session.query(Tag).filter(Tag.id.in_((tag_id[1],))).first()
        tags.append(tag)

    return tags


@app.get("/api/tag/{name}")
async def get_tag(name):
    tag = session.query(Tag).filter(Tag.name.in_((name,))).first()

    return tag


@app.post("/api/article/post")
async def post_article(request: PostArticleData):
    data = request.data
    username = data["login"].name
    password = data["login"].password
    query = session.query(User).filter(User.name.in_((username,))).first()

    if query is not None:
        if not verify_password(password, query.password):
            return 401
    else:
        return 401

    article = Article()
    article.title = data["article"].title
    article.slug = data["article"].slug
    article.text = data["article"].text

    if data["article"].tags != []:
        for name in data["article"].tags:
            article.tags.append(Tag(name=name))
            
    session.add(article)
    session.commit()

    return 200
