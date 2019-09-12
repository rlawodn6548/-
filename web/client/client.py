import time
from socket import *

def receiveHeader(data):
    count=0
    msg_list=[]
    msg=""
    for ele in data:
        if ele=='^':
            msg_list.append(msg)
            msg=''
        else:
            msg = msg + ele
    msg_list.append(msg)
    return msg_list

if __name__=='__main__':
    f = open("version.txt", 'r')
    date = f.readline()
    print(date)
    f.close()

    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('192.168.31.171', 8001))  # 소켓 연결

    print('연결 확인 됐습니다.')
    clientSock.send(date.encode('utf-8'))  # version(date)전송

    number_of_file = int(clientSock.recv(1024).decode())  # 수정해야할 파일 갯수 수신
    print(str(number_of_file) + "개")

    print('수신완료.')

    while number_of_file > 0:
        number_of_file = number_of_file - 1
        header = clientSock.recv(1024).decode()
        data = list(header)
        data_list = receiveHeader(data)

        filename = str(data_list[0])
        ext = str(data_list[1])
        age = str(data_list[2])
        gender = str(data_list[3])
        print(filename)
        print(ext)
        print(age)
        print(gender)
        data_transferred = 0
        file_data = clientSock.recv(1024)
        if not file_data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생')
        with open('download/' + filename, 'wb') as f:
            try:
                while file_data:
                    f.write(file_data)
                    data_transferred += len(file_data)
                    file_data = clientSock.recv(1024)
            except Exception as e:
                print(e)
