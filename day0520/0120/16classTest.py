
import time

class MyClass:
    var = '안녕하세요 둘리'

    def __init__(self, name):
        print('\n생성자~~~~~~~~~')
        print(name, '님 환영합니다')
        print(self.var)

    
    def __del__(self):
        print('MyClass 소멸자 호출확인 12:17 12:19') 
        

    def sayHello(self):
        print('sayHello함수')
        print(self.var)

class Child(MyClass):
    def calculator(self,a,b):
         c=a+b
         return c 
    
obj = Child('aa')
ret1=obj.calculator(2,3); print(ret1)
ret2=obj.calculator(7,8); print(ret2)

#115페이지 클래스상속 다중상속도 가능함 
#114페이지 클래스상속  class 자식이름(부모클래스)

#113페이지 class = 전역변수 + 생성자(self)  + 일반함수(self) + 소멸자 
#111페이지 class = 전역변수 + 생성자(self)  + 일반함수(self) 
#자바접근 MyClass  obj = new MyClass();
#파이썬  obj =  MyClass();
#print(obj) #<__main__.MyClass object at 0x000002AEDEF98F50>





print()