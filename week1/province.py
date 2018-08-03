# Create by dingshuangdian


#省市区三级联动练习


import json
flagProvice=True
flagCity=True
flagArea=True
countProvice=1
countCity=1
countArea=1
proviceList=[]
cityList=[]
areaList=[]
with open("province.txt",encoding='UTF-8') as f:
    areaMsg=json.load(f)
    for provice in areaMsg:
        proviceList.append(provice["region"])
    print(proviceList)
    selectProvice=input("请选择省市:")
    while flagProvice:
        for sProvice in areaMsg:
            if selectProvice == sProvice["region"]:
                for city in sProvice["regionEntitys"]:
                    cityList.append(city["region"])
                print(cityList)
                selectCity=input("请选择城市:")
                while flagCity:
                    for sCity in sProvice["regionEntitys"]:
                        # noinspection PyInterpreter
                        if selectCity==sCity["region"]:
                            for selectArea in sCity["regionEntitys"]:
                                areaList.append(selectArea["region"])
                            print(areaList)
                            selectArea = input("请选择城区:")
                            while flagArea:
                                for sArea in areaList:
                                    if selectArea==sArea:
                                        print("您选择了:",selectProvice,selectCity,selectArea)
                                        flagArea=False
                                        break
                                    countArea+=1
                                if (countArea > len(areaList)):
                                    selectArea = input("城区输入有误，请重新输入:")
                                    countArea = 1
                            flagCity = False
                            break
                        countCity+=1
                    if (countCity > len(cityList)):
                        selectCity = input("城市输入有误，请重新输入:")
                        countCity = 1
                flagProvice = False
                break
            countProvice+=1
        if(countProvice>len(proviceList)):
            selectProvice = input("省份输入有误，请重新输入:")
            countProvice=1












