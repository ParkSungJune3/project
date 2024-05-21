dan = 34
#문제1  for반복문
print('for반복문')
for i in range(1,10):
    #print(dan,'*',i,'=',(dan*i))
    #print('{} * {} = {}'.format(dan,i,(dan*i)))
    print(f'{dan} * {i} = {(dan*i)}')

#문제2  while반복문
print()
print('\nwhile반복문')
cnt = 0 
while True:
  cnt = cnt + 1  
  print(f'{dan} * {cnt} = {(dan*cnt)}')
  if cnt==10:
     break

