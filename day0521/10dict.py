mysite  = { 1:'네이버', 2:'카카오' } #딕트 dict
print(mysite) #{1: '네이버', 2: '카카오'}

#해결1] 항목추가 3 파이썬  add(),append(),insert(1위치,2값) 사용못함
mysite[3] = '파이썬'
print(mysite)
#해결2]  1값을 아마존
mysite[1] = '아마존'
print(mysite)

print('-' * 100 )
#해결3]  2값 카카오 출력만
print(mysite[2])     #[키값]
print(mysite.get(2)) #get()함수로 접근 

print()
#해결4]  3,5값 있는지 체크 in 
print( 5 in mysite ) #False
print( 3 in mysite ) #True
















print()