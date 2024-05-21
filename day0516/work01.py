#문제 해결  12시 15분까지 

name = ''
age = 0
fit = 0.0

#문제 
#input() 이름,나이,fit입력받고, 형변환 str(), int(), float()/ list(),tuple(),set(),dict()
#예외처리 try:  ~ except: 
#print()출력
#12시20분 자바 이클립스실행 
name=str(input('이름입력>>> ')) #문자열변환 str()
age= int(input('나이입력>>> ')) #정수형변환 int( input('안내문'))
fit=float(input('fit입력>>> ')) #실수형변환 float( )

if age < 19 :
    msg = '미성년'
else:
    msg= '어른'

print(name)
print(age)
print(fit*2.1)

print()





