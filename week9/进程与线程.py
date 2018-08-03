# Create by dingshuangdian


import threading
import time


# 多线程
def run(n):
    print("task", n)
    time.sleep(2)


start_time = time.time()
t_objs = []
for i in range(100):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()
print("----------------all threads has finished...")
print("cost:", time.time() - start_time)

#
# class MyThread(threading.Thread):
#     def __init__(self, n):  # 初始化，父类的构造函数
#         super(MyThread, self).__init__()  # 重构继承
#         self.n = n
#
#     def run(self):
#         print("runnint task", self.n)
#
#
# t1 = MyThread("t1")
# t2 = MyThread("t2")
# t1.start()
# t2.start()
