#파일처리

path = 'C:/Mtest/aaa.txt'
file = open(path, 'w', encoding='utf-8')
name =input('이름>>> ')
age =input('나이>>> ')
juso =input('주소>>> ')

file.write(name+'\n')
file.write(age+'\n')
file.write(juso+'\n')
file.close() #권장
print(path, '파일저장 성공했습니다 ')


'''
path = 'C:/Mtest/aaa.txt'
wfile = open(path, 'w', encoding='utf-8')  #쓰기
rfile = open(path, 'r', encoding='utf-8')  #읽기
afile = open(path, 'a', encoding='utf-8')  #존재하면 뒤쪽추가

with open(path, 'w', encoding='utf-8') as myfile:
    pass
    #myfile.함수()

페이지참고
# O'REILLY교재 122페이지 파일처리
    변수  = open(파일, w/r/a모드, 인코디) ~~ close()권장
    ㄴ O'REILLY교재 124페이지 파일모드 
   ㄴ 피클
    ㄴ json드디어 등장  
    ㄴ O'REILLY교재 128페이지 파일모드   with  open() as 대표자: ~~~~ close생략가능

# O'REILLY교재 126페이지 파일함수 read(), write(1)

# 200제 예제 226페이지 ~ 252페이지 실습
'''