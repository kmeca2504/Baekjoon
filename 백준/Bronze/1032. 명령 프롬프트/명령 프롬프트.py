num = int(input()) #파일이름의 개수를 입력 받는다.
word = list(input()) #파일의 이름을 list로 입력 받는다.

for i in range(1,num) :#입력받은 파일이름의 개수만큼 반복한다.
    word2 = input() #파일 이름을 입력받는다.
    for n in range(len(word)):#파일의 글자수만큼 반복한다.
        if word[n] == word2[n]:#파일의 이름과 입력받는 파일이름의 배열이 같을경우.
            continue#계속
        else:#파일의 이름과 입력받는 파일의 배열이 다를 경우
            word[n] = "?"#다른 배열의 위치를 ?로 변환한다.

print(*word,sep= "")#출력