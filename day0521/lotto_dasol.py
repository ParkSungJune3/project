import random


lotto = []

while len(lotto) != 6:
    a = random.randint(1, 45)
    while True:
        if lotto.count(a) == 1:
            a = random.randint(1, 45)
        else:
            lotto.append(a)    
            break
lotto.sort()
print(lotto)
        
    