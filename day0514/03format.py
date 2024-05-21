# 03format.py

a,b,ret = 7,4,0 
ret = a * b 

print(a,'*',b,'=',ret)
print('%d * %d = %d' %(a,b,ret))  #%d  %c  %s  %f
print('{} * {} = {}'.format(a,b,ret)) #format함수
print(f'{a} * {b} = {ret}') 

print('\n')