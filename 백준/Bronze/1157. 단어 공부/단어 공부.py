#단어 공부문제

text = input().upper() #text를 입력을 받으면서 전체문자를 대문자로 변환하여 변수에 저장한다.
text_list = list(set(text)) #비교를 하기위해 set함수를 사용하여 중복된 문자값을 제거한 후 변수에 저장한다.

cnt = [] # 각문자의 등장 횟수를 저장할 리스트를 초기화한다.
for i in text_list: #중복제거된 문자 각각에 대하여
    count = text.count # 'text'에서 각 문자의 등장 횟수를 세는 함수를 'count'에 할당한다.
    cnt.append(count(i)) #해당문자의 등장 횟수를 'cnt'리스트에 추가

if cnt.count(max(cnt)) > 1: # 두개 이상의 문자가 가장 많이 등장하는 경우
    print("?")#?를 출력한다.

else:
    print(text_list[(cnt.index(max(cnt)))]) # 가장 많이 등장하는 문자를 출력한다.