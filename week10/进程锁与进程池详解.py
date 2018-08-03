# Create by dingshuangdian
from multiprocessing import Process, Pool, freeze_support
import time
import os


# 进程池

# 启动多进程必须 if __name__=='__main__':当作模块不执行该条件下的方法，否则执行

def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exex done:', arg, os.getpid())  # 回调


if __name__ == '__main__':
    pool = Pool(processes=3)  # 允许进程池同时放入3个进程
    print("主进程", os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback=回调

    print('end')
    pool.close()  # 一定要关闭进程池再join。
    pool.join()  # 进程池中执行完毕再关闭，如果注释，那么程序直接关闭
