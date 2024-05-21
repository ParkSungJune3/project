# 02date.py
# O'REILLY교재 75페이지 
# import datetime  #dt = datetime.datetime.now()
from datetime import datetime  #dt = datetime.now()
import time

dt = datetime.now()
print(dt)
print()
time.sleep(1)
ob = time.localtime() 
#print(ob)
print(ob.tm_year,'년 ', ob.tm_mon, '월', ob.tm_mday, '일')
print()


#76page페이지 함수 기술 







