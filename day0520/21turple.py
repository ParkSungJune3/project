# O'REILLY교재 83페이지
su = [5, 46, 7, 9, 71, 24]
pos = ( '시청', 36.73982, 127.92851 ) #중복가능,값변경안됨
print(su)   #list[]
su[1]=600
print(su);print()

#문제1] su리스트 46값 600변경
#문제2] pos튜플 값변경안됨 36.73982값 92.12381변경

print(pos)  #tuple()
#실행중에러 변경불가 pos[1]=92.12381
print(pos)