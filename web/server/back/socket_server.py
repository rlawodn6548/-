import os
from socket import *
from os.path import exists
from select import *
import pymysql
import time

HOST = ''
PORT = 8001
BUFSIZE = 1024
ADDR = (HOST, PORT)


def makeheader(filename, ext, age, gender, filesize):
    filename = '%-100s' % filename
    ext = '%-8s' % ext
    age = '%-3s' % age
    gender = '%-10s' % gender
    filesize = '%-20s' % filesize
    #msg = filename + "^" + ext + "^" + age + "^" + gender
    msg = filename + ext + age + gender + filesize
    header = '%-1024s' % msg
    print("len = " + str(len(header)))
    print("header = " + header)
    return header


def sendfile(filename, filepath):
    data_transferred = 0


    if not exists(filepath):  # 파일이 해당 디렉터리에 존재하지 않으면
        print('not exist')
        return  # handle()함수를 빠져 나온다.


    print('파일[%s] 전송 시작...' % filename)
    with open(filepath, 'rb') as f:
        try:
            data = f.read(1024)  # 파일을 1024바이트 읽음
            while data:  # 파일이 빈 문자열일때까지 반복
                clientSocekt.send(data)
                data_transferred += len(data)
                data = f.read(1024)
        except Exception as e:
            print(e)

    print('전송완료[%s], 전송량[%d]' % (filename, data_transferred))


# 매개변수는 모두 str type
def findpath(filename, age, gender):
    sql = "SELECT filepath FROM ad_file_table WHERE filename = '" + filename + "' AND age = '" + age + "' AND gender = " + gender + "'"
    ##
    return 0


#DB 연결
conn = pymysql.connect(host='localhost', user='root', password='111111', db='face_ad', charset='utf8')
curs = conn.cursor()

# = input('다운로드 받은 파일이름을 입력하세요:')
#getFileFromServer(filename)

# 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
print("<server socket>")
print(ADDR)
print(serverSocket)

# 소켓 주소 정보 할당
serverSocket.bind(ADDR)
print('bind')



while 1:
    # 연결 수신 대기 상태
    serverSocket.listen(100)
    print('listen')

    # 연결 수락
    clientSocekt, addr_info = serverSocket.accept()
    print('accept')
    print('--client information--')
    print(clientSocekt)

    recent_date = clientSocekt.recv(1024)
    if not recent_date:
        print('error#01')
        exit()

    print('recv_data: ' + recent_date.decode())

    #loading_update_file(recent_date)
    sql = "SELECT * FROM ad_file_table WHERE upload_date BETWEEN '" + recent_date.decode() + "' AND NOW()"
    #print(sql)
    curs.execute(sql)
    rows = curs.fetchall()
    rows_len = len(rows)
    clientSocekt.sendall(str(rows_len).encode())

    age = ''
    gender = ''

    # 메세지 1개 파일 1개 전송
    for row in rows:
        #print(row)
        filename = row[0]
        ext = row[1]
        age = row[4]
        gender = row[5]

        filepath = row[3]
        filepath = filepath[1:]
        filepath = "C:/Bitnami/wampstack-7.3.8-0/apache2/htdocs" + filepath + filename
        print('filepath = ' + filepath)
        filesize = os.path.getsize(filepath)

        # 메세지 전송
        message = makeheader(filename, ext, age, gender,filesize)
        clientSocekt.send(message.encode())

        # 파일 전송
        sendfile(row[0], filepath)      #row[0] = filename
        #time.sleep(1) # sleep

    print("rows_len = " + str(rows_len))
    print("socket disconnet")
    clientSocekt.close()

# DB Connection 닫기
conn.close()