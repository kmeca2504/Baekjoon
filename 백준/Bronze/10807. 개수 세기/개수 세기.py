'''

프로젝트 명 : 개수 세기
프로젝트 일시 : 2023.08.09 

문제 : 총 N개의 정수가 주어졌을 때, 정수 v가 몇개인지 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 정수 개수 N(1<= N <= 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 V가 주어진다.
        입력으로 주어지는 정수 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

'''

n = int(input())
n_list = list(map(int,input().split()))
v = int(input())

print(n_list.count(v))