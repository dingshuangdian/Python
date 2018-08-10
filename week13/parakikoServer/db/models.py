# Create by dingshuangdian

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func, DATE, ForeignKey,Enum
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import ChoiceType,PasswordType



Base = declarative_base()


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    def __repr__(self):
        return self.name


class RemoteUser(Base):
    __tablename__='remote_user'
    id=Column(Integer,primary_key=True)
    auth_type=Column(Enum(0,1))
    username=Column(String(32))
    password=Column(String())


class UserProfile(Base):
    pass


class AuditLog(Base):
    pass
