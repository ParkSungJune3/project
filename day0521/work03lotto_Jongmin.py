import random

lotto=[]

while len(lotto)!=6:
    lotto.append(random.randint(1,45))
    for a in range(len(lotto)):
        if(lotto.count(lotto[a])>1):
            lotto.pop()
            lotto.append(random.randint(1,45))

# print(lotto)
lotto.sort()
print(lotto)