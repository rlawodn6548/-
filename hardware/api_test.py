import os
import sys
import requests
client_id = "T9kpyfrV7JPYMpwRxRCl" #naver api 아이디
client_secret = "g__6vWyhbi"    #naver api 비밀번호
url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
files = {'image': open('bald.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)