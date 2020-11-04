from flask import Blueprint, request, abort, jsonify

admin = Blueprint('admin', __name__)

@admin.route('/init_db')
def init_db():
    from app.libs.db import get_db_engine
    from app.models import Article, User

    db_engine = get_db_engine()

    User.User.__table__.create(db_engine, checkfirst=True)
    Article.Article.__table__.create(db_engine, checkfirst=True)

    return 'True'
