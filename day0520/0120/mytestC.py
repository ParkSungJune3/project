#myTestA.py

#103페이지  import 접근 모듈접근 
import LG  as my  
import time

print('myTestC.py LG모듈import as my \n')
print('계정id ' ,my.user_id)
print('계정pw ',my.user_pwd)
print()

time.sleep(1) #지연시간 1초
my.note('독도', 2700) #매개인자
time.sleep(1)
my.game()  #일반함수