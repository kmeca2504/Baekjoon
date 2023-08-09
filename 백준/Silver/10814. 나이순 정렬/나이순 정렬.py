import sys
x = int(input())

arr = []

for i in range(x):
    age,name = map(str,sys.stdin.readline().split())
    arr.append([int(age),i,name]) # i를 추가한 이유는 입력 받은 순서대로 정렬을 하기 위해서

arr.sort()
for i in range (len(arr)):
    print("%d %s " % (arr[i][0],arr[i][2]))