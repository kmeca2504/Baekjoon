x = int(input()) #실수를 입력받음

for i in range(1,x): #range()함수를 활용해서 1부터 x까지의 반복한다.
    print(' '*(x-i) + '*'*(2*i-1)) #출력
for i in range(x,0,-1): #range함수를 활용해서 x부터 0까지 반복한다. 
    print(' '*(x-i)+'*'*(2*i-1)) #출력