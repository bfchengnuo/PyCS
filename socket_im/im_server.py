import json
import socket
import threading
from collections import defaultdict

# 维护用户连接
# 使用 defaultdict 代替 dict，当调用的 key 不存在进行赋值时，自动初始化 val 为 dict
# d['a']['b'] = 123  // a 不存在时，b 初始化为 dict；参数可以是任何函数，函数返回什么默认就初始化为什么
online_users = defaultdict(dict)

# 维护历史消息
user_msgs = defaultdict(list)

server = socket.socket()
# bind ip
server.bind(("0.0.0.0", 7878))
server.listen()


def handle_socket(sock: socket, addr):
    while True:
        data = sock.recv(1024)
        # print(data.decode("utf8"))
        json_data = json.loads(data.decode("utf8"))
        action = json_data.get("action", "")
        if action == "login":
            online_users[json_data["user"]] = sock
            sock.send("登陆成功".encode("utf8"))
        elif action == "user_list":
            # 列表生成式
            users = [user for user, soct in online_users.items()]
            sock.send(json.dumps(users).encode("utf8"))
        elif action == "history_msg":
            # if json_data["user"] in action:
            sock.send(json.dumps(user_msgs.get(json_data["user"], [])).encode("utf8"))
        elif action == "send_msg":
            if json_data["to"] in online_users:
                online_users[json_data["to"]].send(json.dumps(json_data).encode("utf8"))
            user_msgs[json_data["to"]].append(json_data["data"])
        elif action == "exit":
            del online_users[json_data["user"]]
            sock.send("已退出".encode("utf8"))
            break


while True:
    # 阻塞
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_socket, args=(sock, addr))
    client_thread.start()
