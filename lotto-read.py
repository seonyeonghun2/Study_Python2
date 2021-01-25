# p.175
import os
import requests

url = 'https://img.hankyung.com/photo/201912/99.11408081.1.jpg'
res = requests.get(url)
img = res.content

with open('images/photo2.jpg', 'wb') as f:
    f.write(img)











'''f = open('lotto.txt', 'w', encoding='utf-8')
line = f.readline()
print(line)'''

# lines = f.readlines()
# for line in lines:
#     print(line)
# f = open('lotto.txt', 'a', encoding='utf-8')
# for i in range(11,20):
#     data = '%d 번째 줄 입니다\n' % i
#     f.write(data)
# f.close()