print()
import time

class MyClass:
    var = '안녕하세요 길동' #클래스영역에서 전역변수 접근키워드 self사용
    def sayHello(self):
        print('sayHello함수')
        print(self.var)

obj =  MyClass()
print(obj.var)
print()

time.sleep(1)
obj.sayHello( )
#106페이지 class = 전역변수 + 생성자  + 일반함수 
#자바접근 MyClass  obj = new MyClass();
#파이썬  obj =  MyClass();
#print(obj) #<__main__.MyClass object at 0x000002AEDEF98F50>





print()