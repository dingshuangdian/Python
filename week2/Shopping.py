# Create by dingshuangdian

shopCar=[("华为P20",8000),("GTX1060 6GB",1999),("Inter core I5 8400",1300),("张召忠说",58),("格力空调",2980)]

shopingList=[]
salary=input("Input your salary:")
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(shopCar):
            print(index+1,item)
        user_choice=input("选择要购买的东西>>>>>:")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<=len(shopCar) and user_choice>=1:
                p_item=shopCar[user_choice-1]
                if p_item[1]<=salary:
                    shopingList.append(p_item)
                    salary-=p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m"% (p_item[0],salary))
                else:
                    print("\033[31;1m你的余额只剩[%s]啦，还买个毛线\033[0m"%salary)
            else:
                print("product code [%s] is not exist!"% user_choice)
        elif user_choice=="q":
            print("---------shoppinglist-----------")
            for p in shopingList:
                print(p)
            exit("您的余额还剩:\033[31;1m%s\033[0m"%salary);
        else:
            print("invakid option")
else:
    print("invakid option")