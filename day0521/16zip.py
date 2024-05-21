a = [11, 22, 33]
b = { 'one', 'two', 'three' }

for value in zip(a,b):
    print(value) #튜플


mysite = { 'aa':'네이버', 'bb':'카카오', 'cc':'파이썬'}
print()
print(mysite.keys())
print(mysite.values())
print(mysite.items())