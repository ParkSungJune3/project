days_list=['Mon','Tue','Wed','Thu','Fri','Sat','Sun', 'Tue' ]
print()
print(days_list)

days_set = set(days_list)
print(days_set) #순서가 흐트러짐
# int(), str(), float(), list()자주사용기술, set()

days_set.add(37) #셋추가는 add()
days_set.add(45) #리스트는 append(), insert(1,2)
print(days_set)
days_set.remove('Wed')
days_set.discard('Mon')
print(days_set)












print()