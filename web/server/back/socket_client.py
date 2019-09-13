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

##now = datetime.datetime.now()
##print(str(now)[0:10])
f = open("version.txt", 'r')
date = f.readline()
print(date)
f.close()

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8001))  # 소켓 연결

print('연결 확인 됐습니다.')
clientSock.send(date.encode('utf-8')) #version(date)전송

number_of_file = int(clientSock.recv(1024).decode()) #수정해야할 파일 갯수 수신
print("update할 파일 : " + str(number_of_file)+"개")

while number_of_file > 0:
    number_of_file = number_of_file - 1

    packet = ''
    header = ''
    remain_data = 1024
    while remain_data > 0:
        packet = clientSock.recv(remain_data).decode()
        header += packet
        remain_data -= len(packet)

    print('length = ' + str(len(header)))
    print('header = ' + header)

    filename = header[0:100].rstrip()
    ext = header[100:108].rstrip()
    age = header[108:111].rstrip()
    gender = header[111:121].rstrip()
    file_size = int(header[121:141].rstrip())

    with open('C:/Users/최태영/PycharmProjects/socket_test1/' + filename, 'wb') as f:
        try:
            while file_size > 0:
                file_data = clientSock.recv(file_size)
                f.write(file_data)
                file_size -= len(file_data)

        except Exception as e:
            print(e)

'''
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
    with open(filename, 'wb') as f:
        try:
            while file_data:
                f.write(file_data)
                data_transferred += len(file_data)
                file_data = clientSock.recv(1024)
        except Exception as e:
            print(e)
    '''

file_info = clientSock
print(file_info)
print('수신완료.')


''' 헤더파일 받는 부분 
while number_of_file > 0:
    header = clientSock.recv(1024)
    number_of_file = number_of_file-1
    print() 
    
'''


'''
data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))
name = data.decode('utf-8')[0:5]
ext = data.decode('utf-8')[5:8]
age = data.decode('utf-8')[8:11]
gender = data.decode('utf-8')[11:]
print(name+"/"+ext+"/"+age+"/"+gender)
'''