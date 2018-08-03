# Create by dingshuangdian
import os
import time
import shlex
import subprocess

import xml.dom.minidom as xmldom
print(">>>>>>>>>>>>>>>>>欢迎进入自动打包系统>>>>>>>>>>>>>>>>>>")
pluginList=[]
def finddir(startdir,target):
    for new_dir in os.listdir(startdir):
         filepath = os.path.join(startdir, new_dir)
         if os.path.isdir(filepath):
             try:
                 os.chdir(filepath)  # 切换目录
             except:
                 return
             for next_ in os.listdir(os.curdir):
                    if next_ == target:
                        xmlfilepath = os.path.abspath(next_)
                        # 得到文档对象
                        domobj = xmldom.parse(xmlfilepath)
                        # 得到元素对象
                        elementobj = domobj.documentElement

                        if elementobj.hasAttribute("id"):
                            pluginList.append(elementobj.getAttribute("id"))
finddir("E:\plugintest","plugin.xml")
dr = input("请输入项目路径:")
os.chdir(dr)
os.system("cmd/c start")
cmd = "ionic serve/c start"
#fhandle = open(r"e:\aa.txt", "w")
os.system(cmd)


# yon=input("是否打入新的插件?(y/n)")
# if yon=="y":
#     for index, item in enumerate(pluginList):
#         print(index + 1, item)
#     nun=input("输入序号选择需要打入的插件>>>>>>>>>>")
#     if nun.isdigit():
#         user_choice = int(nun)
#
#
# else:
#     print("开始执行打包命令>>>>>>>")
#
# p = subprocess.Popen("cmd/c start", stdin=subprocess.PIPE)
# a = p.stdin.write('yes')






