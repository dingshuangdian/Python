# Create by dingshuangdian

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from week12 import orm多外键

session_class = sessionmaker(bind=orm多外键.engine)
session = session_class()

# addr1 = orm多外键.Address(street="Tiankongyuan", city="cangping", state="BJ")
# addr2 = orm多外键.Address(street="laibing", city="guangx", state="guangxsheng")
# addr3 = orm多外键.Address(street="guangz", city="guangd", state="guangdongs")
# session.add_all([addr1, addr2, addr3])
# c1 = orm多外键.Customer(name="Mr.D", billing_address=addr1, shipping_address=addr2)
# c2 = orm多外键.Customer(name="Mrs.L", billing_address=addr3, shipping_address=addr2)
# session.add_all([c1, c2])
obj = session.query(orm多外键.Customer).filter(orm多外键.Customer.name == "Mr.D").first()
print(obj.name, obj.billing_address, obj.shipping_address)
session.commit()
