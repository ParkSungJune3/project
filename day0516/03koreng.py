#03koreng.py
kor=90
eng=85
hap=0
avg=0.0
msg='안내문'
grade='F'

#순서1]  총점,평균
hap = kor + eng
avg = hap/2

#순서2]  if~else 평균점수 70점부터 축합격, 0~69 재시험
if avg >= 70:
    msg='축합격'
else:
    msg='재시험'

#순서3]  if~elif~else 평균점수 100~90 A, 89~80 B, 79~70 C 69~60 D, 59~0 F
if avg >= 90:
    grade='A'
elif avg >= 80:
    grade='B'
elif avg >= 70:
    grade='C'
elif avg >= 60:
    grade='D'
else:
    grade='F'


print('국어 = ', kor)
print('영어 = ', eng)
print('합계 = ', hap)
print('평균 = ', avg)
print('학점 = ', grade)
print('결과 = ', msg)
print('03koreng.py문서')
print()



