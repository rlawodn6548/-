import socketserver

HOST = ''
PORT = 8017

class MyTcpHandler(socketserver.BaseRequestHandler):
    def sendheader(self,filename,ext,age,gender):
        msg = filename + "^" + ext + "^" + age + "^" + gender
        print(msg)
        return msg

    def handle(self):
        print('[%s] 연결됨' % self.client_address[0])
        sock = self.request
        for ele in range(3):
            filename = filenames[ele]
            ext = exts[ele]
            age = ages[ele]
            gender = genders[ele]
            msg = self.sendheader(filename, ext, age, gender)
            sock.send(msg.encode())

            data = sock.recv(1024)
            if not data:
                print('파일을 전송 받지 못함')
                return
            else:
                data = list(data.decode())
                print(data)

        sock.close()
        print('[%s] 끊어짐' % self.client_address[0])


def runServer():
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")

    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++파일 서버를 종료합니다.++++++')

if __name__=='__main__':
    filenames=["filename1","filename2","filen3"]
    exts=["ext1","ext2","ex3"]
    ages=["age1","age2","ag3"]
    genders=["gender1","gender2","gener3"]
    runServer()