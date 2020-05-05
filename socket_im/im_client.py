import socket
import json
import threading

client = socket.socket()
client.connect(("127.0.0.1", 7878))

user = "mps"
login_tmp = {
    "action": "login",
    "user": user
}

client.send(json.dumps(login_tmp).encode("utf8"))
res = client.recv(1024).decode("utf8")
print(res)

# 获取在线用户
getuser_tmp = {
    "action": "user_list"
}
client.send(json.dumps(getuser_tmp).encode("utf8"))
res = client.recv(1024).decode("utf8")
print("在线用户：", res)

# 获取历史消息
history_tmp = {
    "action": "history_msg",
    "user": user
}
client.send(json.dumps(history_tmp).encode("utf8"))
res = client.recv(1024).decode("utf8")
print("历史消息：{}".format(res))

is_receive = True


def handle_receive():
    while is_receive:
        try:
            res = client.recv(1024).decode("utf8")
        except:
            # exit
            break
        try:
            res_json = json.loads(res)
            msg_from = res_json["from"]
            msg = res_json["data"]
            print("收到来自 {} 的信息：{}".format(msg_from, msg))
        except:
            print(res)


def handle_send():
    while True:
        # TODO 其他异常分支暂不处理
        op_type = input("1.发送消息；2.退出；3.查看在线用户；\n")
        if op_type == "1":
            to_user = input("输入要发送到的用户：")
            to_msg = input("输入要发送的内容：")
            send_tmp = {
                "action": "send_msg",
                "from": user,
                "to": to_user,
                "data": to_msg
            }
            client.send(json.dumps(send_tmp).encode("utf8"))
        elif op_type == "2":
            exit_tmp = {
                "action": "exit",
                "user": user
            }
            client.send(json.dumps(exit_tmp).encode("utf8"))
            client.close()
            is_receive = False
            break
        elif op_type == "3":
            client.send(json.dumps(getuser_tmp).encode("utf8"))


if __name__ == "__main__":
    send_thread = threading.Thread(target=handle_send)
    send_thread.start()
    receive_thread = threading.Thread(target=handle_receive)
    receive_thread.start()
