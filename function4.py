# p. 162 매개변수에 초기값 지정하기(기본 매개변수)

# 1. 함수의 정의 <-- 메모리에 상주, 호출할때까지 대기
def say_myself(name, old, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나의 나이는 %d살 입니다.' % old)
    if man:
        print('남성입니다.')
    else:
        print('여성입니다.')

# 함수의 호출
say_myself('박응용', 27)
say_myself('박응용', 27, False)

# 주의 p.163
# 매개변수의 기본값(=기본 매개변수)을 지정할 경우, 매개 변수보다 뒤에 위치해야한다.
# 그렇지 않으면 syntaxError를 발생한다.


# p. 159
# 키워드 매개변수(**) vs 가변 매개변수(*)
# keyword argument --> 키워드 인수 ---> kwargs
def kwargs(**kwargs):
    print(kwargs)

print(kwargs(a=1))
