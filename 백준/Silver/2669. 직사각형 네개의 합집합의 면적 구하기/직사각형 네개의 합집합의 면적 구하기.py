list = [[0 for _ in range(101)] for _ in range(101)] #모든 x좌표와 y표가 1 ~ 100까지인 정수를 참고

for i in range(4): # 4 x 4의 각각의 꼭짓점을 받아오기위한 반복문
    x1, y1, x2, y2 = map(int,input().split()) 

    #map에 면적을 채우기 위한 반복문
    for i in range(x1, x2):
        for j in range(y1, y2):
            list[j][i] = 1

area = 0 #면적의 총합을 계산하기 위한 변수
for k in list:
    area += sum(k) #각각의 면적의 합
print(area) #면적의 총합 출력