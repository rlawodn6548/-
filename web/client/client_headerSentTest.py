import socket

HOST = '192.168.1.8'
PORT = 8017


def receiveHeader(data):
    count = 0
    msg_list = []
    msg = ""
    for ele in data:
        if ele == '^':
            msg_list.append(msg)
            msg = ''
        else:
            msg = msg + ele
    msg_list.append(msg)

    return msg_list


def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print("connect")
        for ele in range(3):
            data = sock.recv(1024)
            if not data:
                print('파일을 전송 받지 못함')
                return
            else:
                print(data.decode())
                data = list(data.decode())

                data_list = receiveHeader(data)

                filename = str(data_list[0])
                ext = str(data_list[1])
                age = str(data_list[2])
                gender = str(data_list[3])

                print(filename)
                print(ext)
                print(age)
                print(gender)
                print()

                msg="ok"
                sock.send(msg.encode())
    return


if __name__ == '__main__':
    connect()