# Create by dingshuangdian
import socket

server = socket.socket()
server.bind(("localhost", 6969))  # 绑定要监听的端口

server.listen()  # 监听
conn, addr = server.accept()  # 等待信息   conn就是客户端连过来而在服务器端为其生成的一个连接实例
data = conn.recv(1024)
print("recv", data.decode())
conn.send(data.upper())
server.close()
