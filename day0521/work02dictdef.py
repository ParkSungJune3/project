import random
import time
import math
import sys   #프로그램종료 sys.exit()

menu = { } 
bl = True
num = 0

def saveMenu():
    name=input('def key메뉴이름>>>')
    price=int(input('value가격입력>>> '))
    menu[name]=price  #등록
    print(name +' 키값 등록 성공했습니다')

def selectAllMenu():
    for k in menu:
        print(k, ':' , menu[k])
    print()

def editMenu():
    name=input('수정key메뉴이름 >>>')
    if menu.get(name)==None:
       print(name ,'수정키 데이터가 없습니다')
    else:
       price=int(input('value수정가격입력>>> '))
       menu[name]=price
       print(name+' 키값 수정 성공했습니다')  

def deleteMenu():
    name=input('삭제key메뉴이름 >>>')
    if menu.get(name)==None:
        print(name ,'삭제키 데이터가 없습니다')
    else:
        menu.pop(name)
        print(name, '데이터삭제 성공했습니다')

def searchMenu():
    name=input('검색key메뉴이름>>> ')
    if menu.get(name) == None:
        print(name, '검색데이터가 없습니다')
    else:
        print(name, ':', menu[name])

def exitMenu():
    print('프로그램을 종료합니다 - 화요일')
    sys.exit()

if __name__=='__main__':
    while bl:
        num = int(input('1.등록  2.출력 3.수정  4.삭제 5.조회 9.종료 >>> '))
        if num==9:
            exitMenu()
        elif num==1:  # 키값=cake/tea/blue/latt/aaa/cock, 가격이 value 450 910 240
            saveMenu()        
        elif num==2:  #전체출력 고전적인방법 for k in menu:
            selectAllMenu()
        elif num==3:  #메뉴key수정, 수정할때 get()결과None일때 수정못함
            editMenu()       
        elif num==4:  #메뉴key삭제, 삭제할때 get()결과None일때 삭제못함
            deleteMenu()
        elif num==5:  #메뉴key조회, 결과None일때 검색못함
            searchMenu()
        else:
            exitMenu()




















print()