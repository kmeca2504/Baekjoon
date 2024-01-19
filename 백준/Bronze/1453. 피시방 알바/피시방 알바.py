# n은 입력받을 숫자의 개수
n = int(input())

# 입력받은 숫자들을 리스트로 저장
input_numbers = list(map(int, input().split()))

# 중복을 제거한 숫자들의 집합 생성
unique_numbers = set(input_numbers)

# 중복된 숫자의 개수 출력
# 전체 리스트 길이에서 중복을 제거한 집합의 길이를 빼면 중복된 요소의 개수가 됨
print(len(input_numbers) - len(unique_numbers))
