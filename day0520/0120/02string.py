#77페이지
data = "i love python"
listdata = ['a','b','c', data]
# print(listdata)
print(data)       #문자열은 그대로 출력i love python
print(list(data)) #['i', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']

for i in range(len(data)): #비권장
    print(data[i], end='')



#73page 문자열슬라이싱 
# data = 'Time is money!!'
# print(data[1:5])
# print(data[:7])
# print(data[9:])
# print(data[-3])
# print(data[:-3])


print()