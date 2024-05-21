# O'REILLY교재 108페이지 enumerate()
order = ( '엘쥐', 78.2, '시청', 23.9, '홍대', 34.5 )  #튜플

for i,v in enumerate(order):
    print(i, ':', v)

#순서명시를 할때 enumerate()
print()
mysite = { 1:'네이버', 2:'카카오', 3:'파이썬'}
for i,k in enumerate(mysite):
    print(i, '번째',k,':', mysite[k])







print()