//시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#include <stdio.h>

int main(){
    int s;
    scanf("%d",&s);
    
    if(s>=90&&100>=s)
        printf("A");
    else if(s>=80&&89>=s)
        printf("B");
    else if(s>=70&&79>=s)
        printf("C");
   else if(s>=60&&69>=s)
        printf("D");
    else
        printf("F");

 return 0;   
}