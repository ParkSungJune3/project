#12for.py문서
#for 대표변수 in range(시작,끝+1,증분)

for a in range(10):
    print(a, end = '\t')
print()

for b in range(1,11,1):
    print(b, end = '\t')
print()

c=0
while c<10:
    c=c+1
    print(c, end = '\t')
print()

d=0
while True:
    d=d+1
    print(d, end = '\t')
    if d==10:
        break




print()
print('-' * 100)