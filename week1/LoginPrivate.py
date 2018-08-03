# Create by dingshuangdian

import json
count=1
userName=input("请输入用户名:")

with open("user.txt") as f:
    userObject = json.load(f)
    for user in userObject:
        if userName == user["userName"]:
            userPassword = input("请输入密码:")
            while count <= 3:
                if userPassword == user["userPassword"]:
                    print("登陆成功!")
                    count=5
                else:
                    userPassword = input("密码错误,请重新输入:")
                    count += 1
            else:
                if count == 4:
                    print("连续输入三次密码错误，账号已被锁定！")
        else:
            print("账号不存在！")






