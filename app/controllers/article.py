from app.models import Article
from app.libs.db import get_db_engine, get_session
from app.libs.article import extract

def add_article(user_id, data):
    article = extract(data['url'])
    session = get_session(get_db_engine())
    result = Article.add_article(session, user_id, article)
    session.close()
    return result

def get_articles(user_id, args):
    session = get_session(get_db_engine())
    articles = Article.get_articles(session, user_id, args.get('page', 1), args.get('keyword', None), args.get('status', None))
    session.close()
    return articles

def get_article(user_id, article_id):
    session = get_session(get_db_engine())
    article = Article.get_article(session, user_id, article_id)
    session.close()
    return article    

def update_article(user_id, article_id, data):
    session = get_session(get_db_engine())
    result = Article.update_article(session, user_id, article_id, data)
    session.close()
    return result

def archive_article(user_id, article_id):
    session = get_session(get_db_engine())
    result = Article.archive_article(session, user_id, article_id)
    session.close()
    return result

def delete_article(user_id, article_id):
    session = get_session(get_db_engine())
    result = Article.delete_article(session, user_id, article_id)
    session.close()
    return result