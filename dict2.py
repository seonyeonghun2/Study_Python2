# p.90 딕셔너리 자료형

dict2 = {
    'name': '김연아',
    'category': '피겨스케이팅',
    'gender': '여성',
    'win': 5,
    'skill': ['트리플 악셀','트리플 플립', '트리플 토룹'],
    'now': '은퇴'
}
dict3 = [
    {
        'name': '김연아',
        'category': '피겨스케이팅',
        'gender': '여성',
        'win': 5,
        'now': '은퇴'
    },
    {
        'name': '류현진',
        'category': '야구',
        'gender': '남성',
        'win': 3,
        'now': '현역'
    },
    {
        'name': '박지성',
        'category': '축구',
        'gender': '남성',
        'win': 5,
        'now': '은퇴'
    }
]


dic = {
    'name': 'pey',
    'phone': '0119993323',
    'birth': '1118',
    'gender': 'female',
    'job': 'artist'
}
# 키만 추출
# dic_keys = dic.keys()

# 값만 추출
# dic_values = dic.values()

#키, 값을 추출
# dic_key_value = dic.items()
# print(dic_keys, type(dic_keys))
# print(dic_key_value, type(dic_key_value))
# for key,value in dic_key_value:
#     print(f'{key} : {value}')
# for dic in dic_values:
#     print(dic)

# 이름 : 종목
athlete = ['김연아','손흥민','류현진','박세리', '손연재']
category = ['피겨스케이팅','축구','야구', '골프', '리듬체조']
total = {}

for i in range(len(athlete)):
    total[athlete[i]]=category[i]

print(total)

'''
'김연아':'피겨스케이팅',
'손흥민':'축구',
'류현진':'야구
'''





