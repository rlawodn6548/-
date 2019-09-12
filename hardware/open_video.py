import random
from moviepy.editor import *
import pygame
import time

def video_open(age, gender): #나이를 입력받아 해당 나이폴더 안에 있는 동영상을 랜덤으로 출력
    try:
        print('age : '+str(age)+' gender : '+gender)
        path='./adv/'+gender+str(age) #해당 나이 폴더로 이동
        print(path)
        file_list = os.listdir(path) #폴더내 파일 리스트 파싱
        print("file_list: {}".format(file_list))
        if not file_list: #폴더내 동영상이 없는 경우
            print('file is empty')
        else:
            adv_num=random.randrange(0,len(file_list)) #랜덤값 생성
            adv_name=file_list[adv_num] #랜덤값에 맍는 파일 이름 파싱
            print(path+'/'+adv_name)
            advtype=adv_name[-3:] #파일이 마지막 3자리 파싱
            print('advtype : '+advtype)
            pygame.display.set_caption(adv_name)  # 동영상 창 타이틀 설정
            clip = VideoFileClip(path + '/' + adv_name)  # 동영상 설정

            if(advtype == 'mp4' or advtype=="avi"): #파일이 mp4나 avi일 경우
                clip.preview() #동영상 실행
            else : #파일이 mp4나 avi가 아닐경우
                clip.preview(fullscreen=True)  #이미지 실행
                time.sleep(5)
            clip.close()
            pygame.quit()

    except :
        print('error ')


if __name__ == "__main__":
    video_open(31,'m')