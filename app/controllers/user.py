from app.models import User
from app.libs.db import get_db_engine, get_session

def add_user(data):
    session = get_session(get_db_engine())
    result = User.add_user(session, data['user_name'], data['password'])
    session.close()
    return result

def get_user(user_id):
    session = get_session(get_db_engine())
    user = User.get_user(session, user_id)
    session.close()
    return user

def update_user(user_id, data):
    session = get_session(get_db_engine())
    result = User.update_user(session, user_id, data['user_name'], data['password'])
    session.close()
    return result

def delete_user(user_id):
    session = get_session(get_db_engine())
    result = User.delete_user(session, user_id)
    session.close()
    return result