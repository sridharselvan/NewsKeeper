import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UserEntity(Base):
    __tablename__ = 'user'

    user_idn = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hash1 = Column(String, nullable=False)
    crt_dt = Column(DateTime, default=datetime.datetime.now)
    upd_dt = Column(DateTime, default=datetime.datetime.now)
    email_id = Column(String, nullable=False)