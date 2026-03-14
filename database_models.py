from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    #inherit from Post
    posts = relationship("Post", back_populates="aligned_user", cascade="all, delete-orphan") # in case of dltng user, its posts will get dltd


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)

    #inherit from User
    user_id = Column(Integer, ForeignKey("users.id"))
    aligned_user = relationship("User", back_populates="posts")














