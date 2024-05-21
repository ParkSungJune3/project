print()


#18list.py
dt=[5,7,33]
print(dt)

dt.append(9)
print(dt)

dt.insert(1, 46) #[5, 46, 7, 33, 9] insert(위치, 데이터)
print(dt) 
print('-' * 100)

ret1 = dt.index(7)
print('7데이터위치 ' , ret1, '번째')


dt.remove(33)
print(dt) #[5, 46, 7, 9]

#dt.remove(2위치가 아니라 값으로 삭제) #2데이터가없으면 에러발생
dt.append(71)
dt.append(24)
dt.append(3)
dt.append(15)
print(dt) #[5, 46, 7, 9, 71, 24, 3, 15]


print(dt[1:4])   #해결1]  46  7  9  추출 슬라이싱 [시작:끝+1]
#del  dt[1:4]    #해결2]  46  7  9  삭제가능
dt[1:4] =[]      #해결2]  46  7  9  삭제가능 
print(dt)


#리스트.remove(값)
#del 리스트[위치]
#del 리스트[시작:끝+1]



print()
