import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')




def datetime_decorater(func):
    def wrapper():
        print('time' + str(datetime.datetime.now())) # 함수 앞에서 실행할 내용
        func()
        print(datetime.datetime.now()) # 함수 뒤에서 실행할 내용
    return wrapper    #closure 함수로 만든다.


@datetime_decorater
def logger_login_david():
    print("Dave login")

#logger_login_david()


#파라미터가 있는 함수에 Decorater 적용하기
def outer_func(function):
    def inner_func(digit1,digit2):
        if digit2 == 0:   #유효성 검사의 예
            print("can't be divided with zero")
            return
        return function(digit1,digit2)
    return inner_func


@outer_func
def divide(digit1,digit2):
    return digit1/digit2

#print(divide(5,3))
#print(divide(5,0))

def type_checker(function):
    def inner_func(digit1,digit2):
        if (type(digit1) != int) or (type(digit2) != int):
            print("integer only")
            return
        return function(digit1,digit2)
    return inner_func

@type_checker
def multiplexer(digit1,digit2):
    return print(digit1 * digit2)

#multiplexer(5,1.1)
#multiplexer(5,'1.1')

#파라미터와 관계없이 모든 함수에 적용 가능한 Decorater 만들기

def general_decorater(function):
    def wrapper(*args,**kwargs):
        print("function is decorated")
        return function(*args,**kwargs)
    return wrapper

@general_decorater
def calc_square(digit):
    return digit * digit

@general_decorater
def calc_plus(digit1,digit2):
    return digit1 + digit2

@general_decorater
def calc_quad(digit1,digit2,digit3,digit4):
    return digit1 * digit2 * digit3 * digit4

#print(calc_square(2))
#print(calc_plus(2,3))
#print(calc_quad(2,3,4,5))

#한 함수에 여러 데코레이터 지정하기
def decorater1(func):
    def wrapper():
        print("decorater1")
        func()
    return wrapper

def decorater2(func):
    def wrapper():
        print("decorater2")
        func()
    return wrapper


@decorater1
@decorater2
def hello():
    print('hello')

#hello()


def mark_bold(function):
    def wrapper(string):
        return '<b>' + function(string) + '</b>'
    return wrapper

def mark_italic(function):
    def wrapper(string):
        return '<i>' + function(string) + '</i>'
    return wrapper

@mark_bold
def contents(string):
    return string

@mark_italic
def contents2(string):
    return string

@mark_bold
@mark_italic
def contents3(string):
    return string

#print(contents('안녕'))
#print(contents2('안녕'))
#print(contents3('안녕'))

def h1_tag(func):
    def func_wrapper(self,*arg,**kwargs):
        return "<h1>{0}</h1".format(func(self,*arg,**kwargs))
    return func_wrapper

class Person:


    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    @h1_tag
    def get_name(self):
            return self.first_name + ' '  +self.last_name

davelee = Person('lee','dave')
#print(davelee.get_name())


# 피라미터가 있는 Decorater 만들기 (심화)

#중첩 함수의 하나 더 깊게 두어 생성
def decorater11(num):
    def outer_wrapper(func):
        def inner_func(*args,**kwargs):
            print('decorater {}'.format(num))
            return func(*args,**kwargs)
        return inner_func
    return outer_wrapper

@decorater11(1)
def print_hello():
    print('hello')

print_hello()
