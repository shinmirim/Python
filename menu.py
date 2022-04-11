import datetime 


print("*디저트 카페에 오신 것을 환영합니다")
print("*주문을 중단하고 싶으시다면 'q'를 눌러주세요")

print("===메뉴판===")
print("디저트류 ==>{'말차갸또쇼콜라':6500, '바스크치즈케이크':6500,'바나나푸딩':5500,'딸기케이크':7000,'얼그레이갸또쇼콜라':6500}")
print("음료 ==>{'아이스아메리카노':4500, '레몬청아이스티':6000, '청포도에이드':4500,'오레오초코':5000}")

dessert ={'말차갸또쇼콜라':6500, '바스크치즈케이크':6500,'바나나푸딩':5500,'딸기케이크':7000,'얼그레이갸또쇼콜라':6500}
drink = {'아이스아메리카노':4500, '레몬청아이스티':6000, '청포도에이드':4500,'오레오초코':5000}

dessertmenu=[]
drinkmenu=[]


while True: 
    selectdessert=input("장바구니에 담고 싶은 디저트 1개를 선택해주세요:")
    
    if selectdessert == 'q':
        break
    else:
        #dessert_list.append({"디저트":dessertmenu,"가격":""})
        dessertmenu.append(selectdessert)
        print(selectdessert,"메뉴가 장바구니에 담겼습니다.\n")
    
    selectdrink= input("장바구니에 담고 싶은 음료 1개를 선택해주세요:")

    if selectdrink =='q':
        break
    else: 
        drinkmenu.append(selectdrink)
        print(selectdrink,"메뉴가 장바구니에 담겼습니다.\n")

print("*장바구니에 담긴 디저트를 알려드립니다*")
print(dessertmenu)
print("*장바구니에 담긴 음료를 알려드립니다*")
print(drinkmenu)

dessertmenu1 =set(dessertmenu)
drinkmenu1= set(drinkmenu)


while True:
    deletemenu = input("장바구니에서 삭제하고 싶은 메뉴 1개를 입력해주세요:")
    
    
    if deletemenu == "q":
        break
    else:
         
        dessertmenu1.discard(deletemenu)
       
        drinkmenu1.discard(deletemenu)
        print(dessertmenu1,drinkmenu1) 
        

    
print("*최종 장바구니*")
print("디저트 : ",dessertmenu1," 음료 : ",drinkmenu1)

print("==========영수증 출력===========\n")

total_menu= dessertmenu1 | drinkmenu1
print("주문시각:",datetime.datetime.now())
print("주문내역:" ,total_menu)

a = 0
for i in dessertmenu1:
    a+= dessert.get(i)

for i in drinkmenu1:
    a+= drink.get(i)

print ("주문하신 메뉴의 총 금액은",a,"원 입니다.")

print("카페를 이용해주셔서 감사합니다.")


#print(totalmenu)



