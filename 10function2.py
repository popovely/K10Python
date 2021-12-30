'''
지역변수 / 전역변수
    : 파이썬에서는 변수 선언시 자료형을 별도로 기술하지 않으므로
      이름이 같아도 지역변수 / 전역변수로 구분된다.

 - 지역변수가 우선순위가 높다.    
'''
# 아래의 total은 서로 다른 변수이다.
total = 0   # 전역변수 선언
def sum(arg1, arg2):
    total = arg1 + arg2 # 지역변수 선언
    print("지역변수 total=", total)
    return total

print("전역변수 total=", total) # 초기값 0이 그대로 출력
print("sum(10, 20)호출후 반환값=", sum(10, 20)) # 합의 결과인 30이 출력
print("==========================================")

'''
내부함수
    : 파이썬은 함수내부에 또다른 함수를 선언할 수 있다.

[형식]
    def 함수명1():
        실행문
        def 함수명2():
            실행문
'''
def commander(saying):
    def inner(quote):   # 내부함수 정의
        return "조선의 위대한 장군 = '%s'" % quote  # 3. 전달받은 값을 반영해 return
    return inner(saying)    # 2.commander()함수의 return문에서 내부함수인 inner()함수 호출
print(commander("이순신"))  # 1. commander()함수 호출
print("==========================================")

'''
매개변수를 전달하는 4가지 방법

1. 순서 매개변수
    : 함수에서 사용하는 일반적인 매개변수. 작성 순서대로 전달
'''
def printme(str1, str2):
    print(str1, str2)
    return
cont = "은 매우 좋은 프로그램입니다."
printme("Python", cont)
print("==========================================")

'''
2. 키워드 매개변수 : 순서와 상관없이 매개변수명에 따라 전달
'''
def printinfo(name, age):
    print("이름:", name)
    print("나이:", age)
    return
printinfo(age=50, name='홍길동')
print("==========================================")
'''
3. 기본 매개변수
    : 인수가 전달되지 않는경우 디폴트로 지정되는 값
'''
def defaultArgs(lan="Java"):
    print("내가 좋아하는 언어는 ", lan, "입니다.")
    return
defaultArgs()   # Java가 출력됨
defaultArgs("C++")  # C++이 출력됨
print("==========================================")
# 만약 JAVA에서의 호출이라면 첫번째 호출문장에서 에러가 발생함. (전달하는 값이 없어서)

'''
4. 가변 매개변수
    : 여러개의 매개변수를 전달해야할 때 사용하는 매개변수.
      JAVA의 가변인자와 비슷함.

 - * : 매개변수의 값을 Tuple로 그룹화
 - ** : 매개변수를 Dictionary로 사용

'''
def product(*args):
    print("*args=>", args)  # Tuple형태로 출력됨
    result = 1
    for a in args:  # tuple이므로 반복문 사용가능
        result *= a # 각 원소를 통해 누적곱을 계산
    return result
print("product(1,2,3,4) =", product(1,2,3,4))

def famousMan(**man):
    print('**man', man) # Dictionary 형태로 출력됨
    for key in man: # Dictionary는 key를 통해 value를 출력
        print(key, "=>", man[key])
famousMan(의인='홍길동', 장군='이순신', 임금='세종대왕')