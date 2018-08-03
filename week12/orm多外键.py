# Create by dingshuangdian

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# 连接数据库
engine = create_engine("mysql+pymysql://uroot:(Itj>G4h)f>d@119.23.57.202/py", encoding="utf-8", echo=True)
# 生成orm基类
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    billing_address_id = Column(Integer, ForeignKey('address.id'))
    shipping_address_id = Column(Integer, ForeignKey('address.id'))

    billing_address = relationship('Address', foreign_keys=[billing_address_id])
    shipping_address = relationship('Address', foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))

    def __repr__(self):
        return self.street


Base.metadata.create_all(engine)
