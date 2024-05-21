#myTestB.py


#101페이지  from ~ import 접근 모듈접근 
#import LG
from LG  import user_id, user_pwd, note, game
from time import sleep

print('myTestB.py LG모듈 from ~ import\n')
print('계정id ' ,user_id)
print('계정pw ',user_pwd)
print()

sleep(1) #지연시간 1초
note('제주도', 34) #매개인자
sleep(1)
game()  #일반함수





