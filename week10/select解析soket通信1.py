# Create by dingshuangdian
import socket
import queue
import select

# select模拟socket server

server = socket.socket()
server.bind(('localhost', 9000))
server.listen(1000)
server.setblocking(False)  # 不阻塞
inputs = [server, ]
outputs = []
msg_dit = {}
while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)
    for r in readable:

        if r is server:  # 代表来了一个新连接
            conn, addr = server.accept()
            print("来了个新连接", addr)
            inputs.append(conn)  # 因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错了，所以要想实现这个客户端发数据来时
            # server端能知道，就需要让select再监测这个conn
            msg_dit[conn] = queue.Queue()  # 初始化一个队列，存储要返回给客户端的数据
        else:
            data = r.recv(1024)
            print("收到数据", data)
            msg_dit[r].put(data)
            outputs.append(r)  # 放入返回的连接队列
            # r.send(data)
            print("send done......")

        for w in writeable:  # 返回给客户端的连接列表
            data_to_client = msg_dit[w].get()
            w.send(data_to_client)  # 返回给客户端的源数据
            outputs.remove(w)  # 确保下次循环的时候writeable，不返回这个已经处理的连接
        for e in exceptional:
            if e in outputs:
                outputs.remove(e)
            inputs.remove(e)
