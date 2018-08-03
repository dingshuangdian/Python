# Create by dingshuangdian

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# 连接数据库
engine = create_engine("mysql+pymysql://uroot:(Itj>G4h)f>d@119.23.57.202/py", encoding="utf-8", echo=True)
# 生成orm基类

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name:%s" % (self.id, self.name)


class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("student.id"))  # 关联外键

    student = relationship("Student", backref="my_study_record")  # 关联student表，通过student查询表student所有数据,

    # Student表通过my_study_record查询表StudentRecord所有数据

    def __repr__(self):
        return "<%s day:%s" % (self.student.name, self.day)


Base.metadata.create_all(engine)  # 创建表结构
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class
# #
Session = Session_class()  # 生成session实例#cursor
# s1 = Student(name="zs", register_date="2018-08-03")
# s2 = Student(name="bs", register_date="2011-08-05")
# s3 = Student(name="cs", register_date="2015-07-03")
# s4 = Student(name="ds", register_date="2019-04-03")
# study_obj1 = StudyRecord(day=1, status="YES", stu_id=1)
# study_obj2 = StudyRecord(day=2, status="NO", stu_id=1)
# study_obj3 = StudyRecord(day=3, status="YES", stu_id=1)
# study_obj4 = StudyRecord(day=1, status="YES", stu_id=2)
# Session.add_all([s1, s2, s3, s4, study_obj1, study_obj2, study_obj3, study_obj4])
stu_obj = Session.query(Student).filter(Student.name == "bs").first()
print(stu_obj.my_study_record)
Session.commit()

# # user_obj1 = User(name="alex", password="qw123456")  # 生成你要创建的数据对象
# # user_obj2 = User(name="d", password="qw1234567")  # 生成你要创建的数据对象
# # print(user_obj1.name, user_obj1.id)  # 此时还没创建对象呢，不信你打印一下id发现还是none
# # Session.add(user_obj1)  # 把要创建的数据对象添加到这个session里，一会统一创建
# # Session.add(user_obj2)
# # Session.commit()  # 现在才统一提交，创建数据。
# # 取所有数据
# data = Session.query(User).filter_by().all()
# # 根据条件取数据
# data1 = Session.query(User).filter_by().first()
# data3 = Session.query(User).filter(User.id == 2).all()
#
# data4 = Session.query(User).filter(User.id > 1).filter(User.id < 3).all()
#
# # 修改,查询出来修改
# # data4.name = "123"
# # data4.password = "qw"
# # Session.commit()
#
#
# # 回滚
# # new_user = User(name='test', password='123')
# # Session.add(new_user)
# # Session.rollback()
#
# # 统计和分组
#
# print(Session.query(User).filter(User.name.in_(['alex', 'd'])).count())
# print(Session.query(User.name, func.count(User.name)).group_by(User.name).all())
#
# # 外键关联
#
# # print(Session.query(User,Student).filter(User.id==Student.id).all())
# # 需要外键关联
# # print(Session.query(User).join(Student).all())
