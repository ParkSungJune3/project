
mysite  = { 1:'네이버', 2:'카카오', 3:'파이썬'}
#출력1] print(mysite)
#출력2] for 반복문 일반적인 접근방법
for k in mysite:
    print(k, ':', mysite[k])

print()
for i,k in enumerate(mysite):
    print(i,'번째' ,k, ':', mysite[k])

print()
for k,v in mysite.items():
    print(k,':', v)





    
    
    
print()