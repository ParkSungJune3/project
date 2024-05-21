#11for.py문서
#for 대표변수 in range(시작,끝+1,증분)
hap = 0
su = 0 
for a in range(1,11,1):
    su +=  1  #대입연산
    print(su, end = '\t')
    hap += su  #대입연산

print('hap = ' , hap)
print()

tot = 0
for k in range(1,11,1):
    print(k, end = '\t')
    tot +=  k #대입연산
print('tot = ' , tot)    
print()
print('-' * 100)