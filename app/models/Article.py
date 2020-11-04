from app.libs.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Enum
from sqlalchemy.sql import func, select
from sqlalchemy.orm import relationship
from app.models.User import User

ROW_PER_PAGE = 10

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1000), nullable=False)
    content = Column(Text, nullable=False)
    link = Column(String(1000), nullable=False)
    top_image = Column(String(100), nullable=False)
    summary = Column(String(2000), nullable=False)
    status = Column(Enum('created', 'updated', 'archived', 'deleted'), nullable=False, default='created')
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

def add_article(session, user_id, data):
    new_article = Article(title=data['title'], 
        content=data['text'], 
        link=data['link'], 
        top_image=data['top_image'], 
        summary=data['summary'],
        user_id=user_id)
    session.add(new_article)
    session.commit()
    session.flush()
    return new_article.id

def get_articles(session, user_id, page, keyword, status):
    stmt = session.query(Article.id, Article.title, Article.top_image, Article.summary)
    
    if keyword:
        stmt = stmt.filter(Article.title.like(f"%{keyword}%"))

    if status:
        stmt = stmt.filter(Article.status == status)
    else:
        stmt = stmt.filter(Article.status != 'archived')

    stmt = stmt.limit(ROW_PER_PAGE).offset((page-1)*ROW_PER_PAGE)
    return stmt.all()

def get_article(session, user_id, article_id):
    return session.query(Article).filter(
        Article.user_id == user_id).filter(Article.id == article_id).first()

def update_article(session, user_id, article_id, data):
    session.query(Article).filter(Article.id == article_id).update({
        "title": data['title'],
        "link": data['link'],
        "summary": data['summary']
    })
    session.commit()
    return True

def archive_article(session, user_id, article_id):
    session.query(Article).filter(Article.user_id == user_id).filter(
        Article.id == article_id).update({
            "status": "archived"
        })
    session.commit()
    return True

def delete_article(session, user_id, article_id):
    session.query(Article).filter(Article.user_id == user_id).filter(
        Article.id == article_id).delete()
    session.commit()
    return True