
dt= [5, 46, 7, 9, 71, 24, 3, 15]
print(dt)

print('추출 ' , dt[1:4])   #해결1]  46  7  9  추출 슬라이싱 [시작:끝+1]
#del  dt[1:4]     #해결2]  46  7  9  삭제가능
#dt[1:4] =[]      #해결2]  46  7  9  삭제가능 
del dt[3:] #한건 데이터값으로 삭제는 remove()
print(dt)
print()
#리스트 함수 append, insert, remove, del키워드, index, sort, reverse, len길이 
#리스트.remove(값)
#del 리스트[위치]
#del 리스트[시작:끝+1]

myhobby=['game',"python", 78.9, 'F',  21 , True]
#해결3] for반복문 출력 
print(myhobby)
for i in range(len(myhobby)):
    #비추천print('[',i,'] =',myhobby[i])
    print(myhobby[i], end=' ')

#해결4] sort(),reverse()
print()
su =  [5, 46, 7, 9, 71, 24, 3, 15]
print(su)
#su.sort()
#print(su)
su.reverse()
print(su)
#리스트는 최대장점 순서가 있고, 중복허용, 많은함수가 제공
#리스트 맨마지막추가 append(), 맨마지막부터 pop()
#리스트 데이터 한번에 삭제 clear()


print()
