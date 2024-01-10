x = int(input()) #테스트 케이스 입력

for i in range(x): #테스트 케이스 만큼 반복
    #input().split()를 사용하는 이유 : 사용자로부터 입력받은 수를 공백 기준으로 분리를 할 수 있다.
    a, b = map(int, input().split()) #테스트 케이스에 대한 정수

    a = a % 10 #정수 a를 컴퓨터 개수 10으로 나눈 값으로 저장.
    
    if a == 0: #나머지가 0일 경우
        print(10) #컴퓨터는 10번 컴퓨터이다.
    elif a == 1 or a == 5 or a == 6: #나머지가 1 또는 5 또는 6일 경우
        print(a) #자기 자신의 값을 출력한다.
    elif a == 4 or a == 9: #4 또는 9일경우  
        if b%2 == 1: #제곱수가 홀수인경우
            print(a) #자기자신 출력
        else: #제곱수가 짝수인 경우
            print((a * a) % 10) # a^2을 10으로 나눈 나머지의 값
    else: #위의 조건들이 아닐 경우
        if b%4== 0: #제곱수가 짝수인 경우
            print((a**4) % 10 % 10 % 10) 
        else:
            print((a**b) % 10 % 10 % 10)