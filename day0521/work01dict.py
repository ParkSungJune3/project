import random
import time
import math
import sys   #프로그램종료 sys.exit()


menu = { } #메뉴이름을 key,  메뉴가격을 value
bl = True
num = 0

while bl:
    print()
    num = int(input('1.등록  2.출력 3.수정  4.삭제 5.조회 9.종료 >>> '))
    if num==9:
        print('프로그램을 종료합니다')
        bl=False
        sys.exit()
    elif num==1:  # 키값=cake/tea/blue/latt/aaa/cock, 가격이 value 450 910 240
        #menu['tea'] = 340
        name=input('key메뉴이름>>>')
        price=int(input('value가격입력>>> '))
        menu[name]=price  #등록
        print(name +' 키값 등록 성공했습니다')
    elif num==2:  #전체출력 고전적인방법 for k in menu:
        for k in menu:
            print(k, ':' , menu[k])
        print()
    elif num==3:  #메뉴key수정, 수정할때 get()결과None일때 수정못함
        name=input('수정key메뉴이름 >>>')
        if menu.get(name)==None:
            print(name ,'수정키 데이터가 없습니다')
        else:
            price=int(input('value수정가격입력>>> '))
            menu[name]=price
            print(name+' 키값 수정 성공했습니다')            
    elif num==4:  #메뉴key삭제, 삭제할때 get()결과None일때 삭제못함
        name=input('삭제key메뉴이름 >>>')
        if menu.get(name)==None:
            print(name ,'삭제키 데이터가 없습니다')
        else:
            menu.pop(name)
            print(name, '데이터삭제 성공했습니다')
    elif num==5:  #메뉴key조회, 결과None일때 검색못함
        name=input('검색key메뉴이름>>> ')
        if menu.get(name) == None:
            print(name, '검색데이터가 없습니다')
        else:
            print(name, ':', menu[name])
    else:
        print('번호를 잘못 입력했습니다\n')
        sys.exit()  #파이썬 >>>> exit()종료

















print()