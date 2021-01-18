# 함수 (p.150)
# 지금까지 - 표현식 <---> 앞으로 - 함수화
# 같은 내용을 반복 <---> 재사용, 반복
# 상수 : 변하지 않는 값
# 함수(코드를 저장)의 정의   vs  변수 (데이터를 저장하는 공간)
'''
# 1. 매개변수가 없는 함수
def 함수의 이름1():
    실행할 코드1
    실행할 코드2
    실행할 코드...

# 2. 매개변수가 있는 함수
# 매개변수(parameter, 파라미터) - 함수 내부에 데이터를 전달하는 변수
# 인수(argument) - 함수 호출할때 전달하는 데이터

def 함수의 이름2(매개변수):
    실행할 코드1
    실행할 코드2
    실행할 코드...
    return 반환값

# 3. 결과값이 없는 함수
def 함수의 이름3(매개변수):
    실행할 코드


함수이름1()    <--- 함수를 호출, 실행
함수이름2(매개변수)   <--- 함수의 호출, 매개변수로 함수 내부에 데이터를 전달
'''
# add - 숫자를 더하고 그 결과값을 알려주는 함수
# 함수 내부로 값을 전달 - 매개변수
# 함수 내부 --> 외부 값을 전달 <--- return
# 반환값이 없는 단순 함수
# ↓ 함수의 정의 - 함수의 이름은 say_hello
def say_hello_10_times():
    for i in range(10):
        print(f'안녕하세요 {i+1}번째 고객님!')

# ↓ 함수의 실행(=호출)
say_hello_10_times()

# 매개변수가 1개인 함수
# print(4**2)
def jegop(x):
    result = x * x
    return result
result_jegop = jegop(5)
print('5의 제곱 : ', result_jegop)
# 매개변수가 2개인 함수 - 매개변수, 인수의 차이
def add(a, b):
    result = a +b
    return result

def sub(a, b):
    if a>b:
        result = a-b
    else:
        result = abs(a-b)
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a // b
    return result

# 매개변수 갯수 --> typeError 발생(매개변수 부족, 초과)
# result_add = add(5, 10, 15)
result_add = add(5, 10)
result_add2 = add(365,5)
result_add3 = add(135,7)
result_add4 = add(32,49)
result_sub = sub(7,3)
result_multiply = multiply(3,10)
result_divide = divide(15, 5)

print('두 10과 5의 합 : '+str(result_add))
print('두 7과 5의 차 : '+str(result_sub))
print('두 3과 10의 곱 : '+str(result_multiply))
print('두 15과 5의 몫 : '+str(result_divide))

print('-'*100)
def new_add(a, b):
    print('%d, %d의 합은 %d 입니다' % (a, b, a+b))

result_new_add = new_add(3,4)
if result_new_add is None:
    print('result_new_add함수는, 반환값이 없습니다')

# None 거짓 (Null 대신 None) <-- 거짓으로 구분