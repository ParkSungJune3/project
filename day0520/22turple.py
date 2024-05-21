# O'REILLY교재 83페이지
su = [5, 46, 7, 9, 71, 24]
pos = ( '시청', 36.73982, 127.92851 ) 
print(pos)   
x,y,z = pos
print(x)
print(y)
print(z)
print()

my = list(pos) #int() , str(), float(),   list(), tuple()
print(my) #리스트
my.append('홍대')
print(my) #리스트
pos = tuple(my)
print(pos)

#에러 pos.append('홍대')  #튜플은 append()X
#에러 pos.insert(2,'합정') #튜플은 insert(1,2)X
#실행중에러 변경불가 pos[1]=92.12381
