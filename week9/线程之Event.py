# Create by dingshuangdian
import threading
import time

event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if count > 20 and count < 30:  # 改成红灯
            event.clear()  # 把标志位清空
            print("\033[41;1mred light is on...\033[0m")
        elif count > 30:
            event.set()  # 变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on...\033[0m")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 代表绿灯
            print("[%s]running..." % name)
            time.sleep(1)
        else:
            print("[%s]sees red light,waiting..." % name)
            event.wait()
            print("\033[34;1m[%s] green light is on start going...\033[0m" % name)


light = threading.Thread(target=lighter, )
light.start()
car1 = threading.Thread(target=car, args=("Tesla",))
car1.start()
