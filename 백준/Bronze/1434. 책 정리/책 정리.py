N, M = map(int, input().split())  # 박스와 책의 개수 입력
boxes = list(map(int, input().split()))  # 각 박스의 용량
books = list(map(int, input().split()))  # 각 책의 크기

current_box = 0  # 현재 박스 인덱스
for book in books:
    # 현재 책이 현재 박스에 들어갈 수 있는지 확인
    while current_box < N and boxes[current_box] < book:
        current_box += 1  # 다음 박스로 넘어감
    if current_box < N:
        boxes[current_box] -= book  # 책을 박스에 넣음

# 낭비된 용량 계산
wasted_capacity = sum(boxes)
print(wasted_capacity)
