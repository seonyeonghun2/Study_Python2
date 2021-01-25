# p.207 모듈(moudule)
# 모듈은 또다른 파이썬 파일이다!
# 모듈 - 표준 모듈(=내장 모듈), [사용자 정의 모듈], 외부 모듈(추가로 설치)
# 모듈 불러오기
'''
1) import 모듈명
2) import 모듈명 as 별명/식별자
3) from 모듈 import 함수명,변수명
※  함수명, 변수명 <----> *
'''
# 1. 표준모듈 math 불러오기
'''import math
print(math.pi)'''

# 2. 터틀그래픽스 불러오기
'''
from turtle import *
※ 가상환경, v3.9.1 오류 [경로, tkinter, 그밖에 잇슈]
'''
# 3. 사용자 정의 모듈
'''from mod1 import add, sub
print('두 수의 합 : ', add(5,4))
print('두 수의 차 : ', sub(10,5))'''


# 4. 외부 모듈
# 4-0) [Terminal] pip list
# 4-1) [Terminal] pip install 모듈이름   / pip uninstall 모듈이름
# ※ pip 버전을 최신으로 업그레이드 하는게 좋다! (의존성)
# 4-2) File > Settings [CTRL+ALT+S] :  Python Interpreter > Module +,-
# requests : HTTP 요청 모듈
import requests
url = 'https://www.daum.net'
req = requests.get(url)
if req.status_code != 200:
    print('응답하지 않습니다')
    exit()
# p.171 파일 읽고 쓰기
f = open('daum.html', 'w', encoding='utf-8')
f.write(req.text)
f.close()
# print(req.text)

