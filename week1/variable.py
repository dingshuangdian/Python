# Create by dingshuangdian

# 变量

# name = "dingshuangdian"
# age = 18
# print("My name is",name,"My age is",age)
import getpass

# name=input("name:")
# age=input("age:")
# job=input("job:")
# salary=input("salary:")

# info='''
# --------------- info of %s ---------------
# Name:%s
# Age:%s
# Job:%s
# Salary:%s
# '''%(name,name,age,job,salary)
# print(info)

# info2='''
# --------------- info of {_name} ---------------
# Name:{_name}
# Age:{_age}
# Job:{_job}
# Salary:{_salary}
# '''.format(_name=name,_age=age,_job=job,_salary=salary)
# print(info2)

# info3='''
# --------------- info of {0} ---------------
# Name:{0}
# Age:{1}
# Job:{2}
# Salary:{3}
# '''.format(name,age,job,salary)
# print(info3)

# password=getpass.getpass("password:")

# apple=25
# count=1 #定义一个计数变量
# while count<=3: #while条件判断，当count<3执行条件语句
#     guess_apple=int(input("apple:"))
#     if guess_apple==apple:
#         print("恭喜，你猜中了！")
#         break; #如果猜中，跳出循环。
#     elif guess_apple>apple:
#         print("没那么多呢，往小点猜~")
#     else:
#         print("快接近了，再往上猜~")
#     count+=1 #每次执行完条件count加1
#
#     if count>3:
#         y_n=input("您已经猜错三次，是否继续？")
#         if y_n!="y":
#             print("游戏结束！")
#         else:
#             count=1#初始化计数变量

# apple=25
# for i in range(3):
#     guess_apple=int(input("apple:"))
#     if guess_apple==apple:
#         print("恭喜，你猜中了！")
#         break; #如果猜中，跳出循环。
#     elif guess_apple>apple:
#         print("没那么多呢，往小点猜~")
#     else:
#         print("快接近了，再往上猜~")
# for i in range(0,10,2):
#     print("loop",i)

