# p.157 입력값이 몇개가 될지 모를때?
# 입력값이 여러개일때!

def add_num(a, b):
    return a+b
result = add_num(5, 9)
print('두 수의 합 : ',result)

# 가변 매개변수 : 매개변수의 갯수가 변한다, 달라진다!
# args, values, items,...변경이 가능하다
def add_many_num(*args):
    result = 0
    for i in args:
        result += i
    return result

multi_result = add_many_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('최종 값 : ',multi_result)

# p.158 여러 매개변수를 곱셈한 결과
def add_calc(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for j in  args:
            # result = result * j
            result *= j
    return result

final = add_calc('add', 1,2,3,4,5,6,7,8,9,10)
print('add 결과 : {0}'.format(final))
final = add_calc('mul', 1,2,3)
print(f'multiply 결과 : {final}')

# Error 1. 기본매개변수 없을때
# final = add_calc(1,2,3,4,5)
# print('기본 매개변수가 없는 결과 : ',final)

# Error 2. 기본매개변수와 가변매개변수의 위치를 바꿨을때
# final = add_calc(1,2,3,4,5,'add')
# print('기본 매개변수와 가변매개변수의 순서를 바꾼 결과 : ',final)

# p.152 명칭/용어 주의!
# 파라미터, 매개변수 <-------------> parameter
# 인수, 인자 <-------------------> argument
# 반환값, 결과값, 돌려주는 값 <----> return












