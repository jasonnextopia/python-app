from app.libs.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Enum
from sqlalchemy.sql import func, select
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    type = Column(String(45), nullable=True)
    created_date = Column(DateTime, default=func.now())
    articles = relationship("Article", backref="user")

def add_user(session, user_name, password):
    new_user = User(user_name=user_name,
        password=password)
    session.add(new_user)
    session.commit()
    session.flush()
    return new_user.id

def get_user(session, user_id):
    return session.query(User).filter(
        User.id == user_id).first()

def update_user(session, user_id, user_name, password):
    session.query(User).filter(User.id == user_id).update({
        "user_name": user_name,
        "password": password
    })
    session.commit()
    return True

def delete_user(session, user_id):
    session.query(User).filter(User.id == user_id).delete()
    session.commit()
    return True