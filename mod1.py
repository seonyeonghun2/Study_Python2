def add(a, b):
    return a + b

def sub(a, b):
    return b - a

def mul(a, b):
    return a * b

# p.210 __name__ 변수의 의미
# print(__name__)
if __name__ == '__main__':
    print(add(1,4))
    print(sub(4,2))
    print(mul(3,5))