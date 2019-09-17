import requests
import cv2
from socket import *
from open_video import video_open
from datetime import datetime

# 카메라에 비친 사람들 중 가장 많은 나이대 추출 함수
def find_age(age, gender):
    for i in range(0, len(age)):
        if len(age[i]) < 5:  # 한자리 숫자 범위 일때 기준값으로 변환
            if 1 <= int(age[i][0:1]) + 2 <= 5:
                age[i] = "1~5"
            elif 6 <= int(age[i][0:1]) + 2 <= 10:
                age[i] = "6~10"
            else:
                age[i] = "11~20"
        if len(age[i]) >= 5:  # 두자리 숫자 범위 일때 기준값으로 변환
            if 11 <= int(age[i][0:2]) + 2 <= 20:
                age[i] = "11~20"
            elif 21 <= int(age[i][0:2]) + 2 <= 30:
                age[i] = "21~30"
            elif 31 <= int(age[i][0:2]) + 2 <= 40:
                age[i] = "31~40"
            elif 41 <= int(age[i][0:2]) + 2 <= 50:
                age[i] = "41~50"
            elif 51 <= int(age[i][0:2]) + 2 <= 60:
                age[i] = "51~60"
            else:
                age[i] = "61~80"
    for i in range(0, len(age)):  # age 배열 앞글자에 성별 붙임
        if gender[i] == "male":
            age[i] = "m" + age[i]
        else:
            age[i] = "f" + age[i]
    data = []
    data.append([age[0], 1])
    flag = 0  # 중복값인지 체크하는 값
    for i in range(1, len(age)):
        for j in range(0, len(data)):
            if age[i] == data[j][0]:  # 중복이면 리스트에 새로운 요소를 추가하지 않고 갯수만 1 증가시킨다
                data[j][1] += 1
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:  # 중복이 아니면 리스트에 새로운 요소 추가
            data.append([age[i], 1])

    ##리스트에서 가장 많은 갯수의 나이대를 추출하는 과정
    value = data[0][1]
    location = 0  # 가장 많은 갯수를 가진 나이대의 리스트상 위치
    for i in range(1, len(data)):  # 비교한다
        if (value <= data[i][1]):
            value = data[i][1]
            location = i
            # 문자열 정수 변환 과정
    if (len(data[location][0]) >= 6):  ##앞자리가 2자리 수 일때
        age_value = int(data[location][0][1:3])
    else:  ##앞자리가 한자리 수일때
        age_value = int(data[location][0][1:2])
    if (data[location][0][0] == 'm'):  # 앞글자를 통해 대표성별 판별
        gender_value = "m"
    else:
        gender_value = "f"

    return (age_value, gender_value)


# 소켓 통신을 통한 업데이트 과정
def socket_update():
    f = open("version.txt", 'r')
    date = f.readline()
    print(date)
    f.close()

    clientSock = socket(AF_INET, SOCK_STREAM)

    try:
        clientSock.connect(('192.168.28.171', 8001))  # 소켓 연결
    except Exception as e:
        print("서버 연결에 실패했습니다")  # 서버 연결 안되어있을시 에러처리
        return;

    print('연결 확인 됐습니다.')
    clientSock.send(date.encode('utf-8'))  # version(date)전송
    number_of_file = int(clientSock.recv(1024).decode())  # 수정해야할 파일 갯수 수신
    print(str(number_of_file) + "개")
    print('수신완료.')

    if number_of_file == 0:
        print("업데이트 할 파일이 없습니다")
        return;

    while number_of_file > 0:
        number_of_file = number_of_file - 1
        packet = ''
        header = ''
        remain_data = 1024;
        while remain_data > 0:
            packet = clientSock.recv(remain_data).decode()
            header += packet
            remain_data -= len(packet)
        '''
        print(header)
        print(len(header))
        print(header[0:100].rstrip())
        print(header[100:108].rstrip())
        print(header[108:111].rstrip())
        print(header[111:121].rstrip())
        print(header[121:141].rstrip())
        print(header[121:141].rstrip())
        '''
        print(header[0:100].rstrip())
        filename = header[0:100].rstrip()
        ext = header[100:108].rstrip()
        age = header[108:111].rstrip()
        gender = header[111:121].rstrip()
        file_size = int(header[121:141].rstrip())
        with open('C:/Users/Park/PycharmProjects/-/adv/' + gender + age + '/' + filename, 'wb') as f:
            try:
                while file_size > 0:
                    file_data = clientSock.recv(file_size)
                    f.write(file_data)
                    file_size -= len(file_data)
            except Exception as e:
                print(e)

    f = open("version.txt", 'w')
    s = datetime.now()
    version = "%04d-%02d-%02d %02d:%02d:%02d" % (s.year, s.month, s.day, s.hour, s.minute, s.second)
    f.write(version)  # 새로운 version 쓰기

    print("---------------------------------------------------------------------")
    print("----------------------UPDATE COMPLETE--------------------------------")
    print("---------------------------------------------------------------------")


########## Main 루트 ##########################
if __name__ == "__main__":
    client_id = "T9kpyfrV7JPYMpwRxRCl"  # naver api 아이디
    client_secret = "g__6vWyhbi"  # naver api 비밀번호
    url = "https://openapi.naver.com/v1/vision/face"  # naver api 주소

    capture = cv2.VideoCapture(0)  # 내장 카메라 사용
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 저장되는 사진의 넓이 사이즈
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 저장되는 사진의 높이 사이즈
    count = 0

    face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')  # opencv에서 얼굴 인식하는 xml
    socket_update()  # 프로그램 구동 전 광고파일들을 업데이트 한다

    while True:
        ret, frame = capture.read()  # 카메라에서 프레임 하나 읽음 ret: 프레임을 제대로 읽었는지 확인 유무 , frame : 읽은 화면

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 카메라에 얼글부분의 사각형을 보여줌
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)  # 카메라 창 생성
        ##cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # 카메라 창 전체화면
        cv2.imshow('window', frame)  # 카메라 화면 보여주기

        if count % 50 == 0:  # 프레임 100번당 1번 opencv에서 얼굴 인식
            count = 0
            if len(faces) != 0:  # open cv에서 사람 인식 한후 밑에 있는 네이버 오픈API 실행
                cv2.imwrite('test.jpg', frame)  # 프레임을 사진으로 저장
                files = {'image': open('test.jpg', 'rb')}  # 사진 열기
                headers = {'X-Naver-Client-Id': client_id,
                           'X-Naver-Client-Secret': client_secret}  # naver api id, pwd를 헤더에 저장
                response = requests.post(url, files=files, headers=headers)  # naver api에 전송 및 응답 받기
                rescode = response.status_code
                result = response.json()  # 응답을 json으로 변환

                if result['info']['faceCount'] == 0:  # 네이버 API에서 사람 인식 못 할때
                    print("person count : ", end='')
                    print(result['info']['faceCount'])  # facecount
                else:  # 네이버 API에서 사람 인식하는 과정
                    print("-----------------------------------------------------------")
                    print("person count : ", end='')
                    print(result['info']['faceCount'])  # facecount
                    age = []
                    gender = []
                    for faceCount in range(len(result['faces'])):
                        print("gender/age : " + result['faces'][faceCount]['gender']['value'] +
                              " / "+result['faces'][faceCount]['age']['value'])  # 인식된 gender 출력
                        age.append(result['faces'][faceCount]['age']['value'])  # 성별 list에 성별 입력
                        gender.append(result['faces'][faceCount]['gender']['value'])  # 나이 list에 나이 입력
                    (age_value, gender_value) = find_age(age, gender)  # 대표 나이 및 성별 결정
                    print("대표 나이 : ", end='')
                    print(str(age_value-1) + "대")
                    print("대표 성별 : ", end='')
                    print(gender_value)
                    print("-----------------------------------------------------------")

                    video_open(age_value, gender_value)  # 성별과 나이에 맞는 광고 출력
            else:  # open cv에서 사람 인식 못했을때
                print("There is no person")

        if cv2.waitKey(1) > 0 : break
        count += 1

    capture.release()
    cv2.destroyAllWindows()
