# p.166 lambda
'''
def 함수명():
    ...실행코드..      <----> lambda 매개변수 : 표현식

'''

def add(a, b):
    return a+b
result = add(4,5)
print('일반함수 : ', result)

# 람다함수 <---> 익명함수
# 자동 return
add = lambda a,b: a+b
final = add(4,5)
print('익명(람다)함수 : ', final)


