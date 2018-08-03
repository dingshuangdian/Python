# Create by dingshuangdian
import socket

client = socket.socket()  # 相当于声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))
client.send("socket学习！！".encode("utf-8"))
data = client.recv(1024)
print("recv", data.decode())
client.close()
