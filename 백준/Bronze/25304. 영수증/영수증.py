#프로젝트 명 : 영수증
#프로젝트 일시 : 2023.08.08 (화)

#문제
#영수증에 적힌, 구매한 각 물건의 각격과 개수, 구매한 물건들의 총 금액을 보고 구매한 물건의 가격과 개수를 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.


sum = 0
i=0
all =int(input())
num =int(input())

while i<num:
    i = i + 1
    price,pNum = map(int, input().split())
    sum = sum + price*pNum
    

if all == sum:
    print("Yes")
else:
    print("No")
