import requests
from bs4 import BeautifulSoup
import time
start = 935
end = 946
for i in range(start, end+1):
    url = f'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={i}회로또'
    res = requests.get(url)
    if res.status_code != 200:
        print('접속이 원할하지 않습니다')
        exit()

    soup = BeautifulSoup(res.text, 'html.parser')
    lotto_numbers = soup.select('.num_box > span')
    lotto = []
    for number in lotto_numbers:
        lotto.append(number.text)
    # p.176~177
    with open('lotto.txt', 'a', encoding='utf-8') as f:
        f.write(str(lotto))
        # escape - new line / 줄바꿈
        f.write('\n')
    time.sleep(3)
print('작업이 완료되었습니다')
