# 03date.py
# O'REILLY교재 76페이지 
# import datetime  #dt = datetime.datetime.now()
from datetime import datetime  #dt = datetime.now()
import time

#리스트 list, 파이썬 리스트는 혼합형 
lotto = [ 23, 7, 19, 45, 31, 26] #int정수형구성 리스트 
mydata = ['kim', 90, 85, 87.5, True, 'B', '축합격'] #혼합리스트 
week = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일' ] #문자열구성 리스트

ob = time.localtime() 
my = ob.tm_wday #숫자출력

print(week[my])  #  print('요일출력 ', my)  
if my==0: 
    print('월요일')
elif my==1: 
    print('화요일')
elif my==2: 
    print('수요일')
elif my==3: 
    print('목요일')
elif my==4: 
    print('금요일')
elif my==5: 
    print('토요일')
elif my==6: 
    print('일요일')




