import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    links = relationship('Link', backref='user', lazy=True, order_by="Link.time")


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer(), primary_key=True)
    url = Column(String(255))
    short_link = Column(String(255))
    time = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer(), ForeignKey('users.id'))
