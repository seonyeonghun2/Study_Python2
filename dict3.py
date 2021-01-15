# 딕셔너리 + 반복문

character = {
    'id': '도끼살인자',
    'job': '기사',
    'level': 99,
    'hp': 1000,
    'mp': 100,
    'skill': ['썰기', '베기', '찌르기', '방패치기'],
    'items': ['검', '방패', '갑옷']
}
print(character)
char_items = character.items()
print(char_items)
for key, value in char_items:
    if type(value) is list:
        # 리스트면~ 어떻게 출력할지
        for el in range(len(value)):
            print(key, ':', value[el])
    else:
        print(key, ':', value)