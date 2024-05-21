#import LG  #import LG물리적인파일명
from LG  import user_id, user_pwd, note, game 
import time
from datetime import datetime

# O'REILLY교재 75페이지 
# zoom.py에서 LG.py문서 전역변수및 함수접근  from ~ import구문 
print('-' * 100)
print('zoom.py 11:37\n')

time.sleep(1) #Thread.sleep(2000=2초), setTimeout(1, 2000=2초)
print(user_id)
print(user_pwd)
print()
time.sleep(1)
note()
time.sleep(1)
game()
print()

dt = datetime.now()
print(dt)
print('-' * 100)
print()
# zoom.py 마지막





