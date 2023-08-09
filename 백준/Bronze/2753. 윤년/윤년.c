#include <stdio.h>

int main(){
    int y;//년도
    scanf("%d",&y); //년도를 받아올 함수
     if ((y % 400) == 0 || ((y % 100) != 0 && (y % 4) == 0))
         printf("1");
    else
        printf("0");
    
return 0;    
}