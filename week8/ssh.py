# Create by dingshuangdian


import socket
import os
import hashlib

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, attr = server.accept()
    print("new conn", attr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        # print("执行指令", data)
        # cmd_res = os.popen(data.decode()).read()  # 接收字符串，执行结果也是字符串
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename, "rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())  # send file size
            conn.recv(1024)  # wait for ack

            for line in f:
                m.updata(line)
                conn.send(line)
            print("file_md5", m.hexdigest())
            conn.send(m.hexdigest().encode())  # send md5
            f.close()

        # if len(cmd_res) == 0:
        #     cmd_res = "cmd has no output..."
        #
        # conn.send(str(len(cmd_res.encode())).encode("utf-8"))  # 先发数据大小给客户端
        # client_ack = conn.recv(1024)
        # conn.send(cmd_res.encode("utf-8"))
server.close()
