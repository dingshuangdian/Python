# Create by dingshuangdian


import socket
import hashlib

client = socket.socket()
client.connect(("localhost", 9999))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server_response:", server_response)
        client.send("ready to recv file")
        file_total_size = int(server_response.decode())
        received_size = 0
        file_name = cmd.split()[1]
        f = open(file_name, "wb")
        m = hashlib.md5()
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size + len(data)
            m.update(data)
            f.write(data)
            print(file_total_size, received_size)
        else:
            new_file_md5 = m.hexdigest()
            print("file recv done", received_size, file_total_size)
            f.close()
            server_file_md5 = client.recv(1024)
            print("server_file_md5", server_file_md5)
            print("server_file_md5", new_file_md5)
# while True:
#     cmd = input(">>:").strip()
#     if len(cmd) == 0: continue
#     client.send(cmd.encode("utf-8"))
#     cmd_res_size = client.recv(1024)  # 接收数据大小
#     print(cmd_res_size)
#     client.send("准备好接收数据了".encode("utf-8"))
#     received_size = 0
#     received_data = b''
#     while received_size < int(cmd_res_size.decode()):
#         data = client.recv(1024)
#         received_size += len(data)  # 每次收到的有可能小于1024，所以必须用len 判断
#         received_data += data
#     else:
#         print(received_size)
#         print(received_data.decode())
client.close()
