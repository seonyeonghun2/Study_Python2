# p.175
import os
import requests

url = 'https://img.hankyung.com/photo/201912/99.11408081.1.jpg'
res = requests.get(url)
# .text : 텍스트 데이터
# .content : 바이너리 데이터
img = res.content

with open('images/photo2.jpg', 'wb') as f:
    f.write(img)
