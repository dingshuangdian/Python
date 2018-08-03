# Create by dingshuangdian

shopCar=[["华为P20",8000],["GTX1060 6GB",1999],["Inter core I5 8400",1300],["张召忠说",58],["格力空调",2980]]
hadBuy=[]
toContinue=True

balance=input("请输入您的账户余额:")
if balance.isdigit():
    balance=int(balance)
while toContinue:
    # for i in shopCar:
    #     print(i.index(i),i)
    for index,i,in enumerate(shopCar):
        print(index+1,i)
    shopNum=input("请选择您要购买的商品(输入商品编号):")
    if shopNum.isdigit():
        shopNum=int(shopNum)
        if balance>=shopCar[shopNum-1][1]:
            balance = balance - shopCar[shopNum-1][1]
            print("您购买了:",shopCar[shopNum-1][0],"账户余额:",balance)
            hadBuy.append(shopCar[shopNum-1])
            y=input("是否继续购买其他商品?(y/n)")
            if y=="y":
                toContinue=True
            else:
                toContinue = False
                print("您购买了:", hadBuy, "账户余额:", balance)

        else:
            y=input("您的账户余额不足,是否选择其它商品？(y/n)")
            if y=="y":
                toContinue = True
            else:
                toContinue = False
                print("您购买了:",hadBuy,"账户余额:",balance)




