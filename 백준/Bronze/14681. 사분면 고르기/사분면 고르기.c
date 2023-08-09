#include <stdio.h>

int main(){
    int x,y; //x좌표 y좌표
    scanf("%d %d",&x ,&y);
    if(x>0&&y>0)
        printf("1");
    if(x<0&&y>0)
        printf("2");
    if(x<0&&y<0)
        printf("3");
    if(x>0&&y<0)
        printf("4");
    
    return 0;
}