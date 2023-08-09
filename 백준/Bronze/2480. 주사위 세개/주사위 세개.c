#include <stdio.h>

int main(){
    int x,y,z; //세개 주사위
    scanf("%d %d %d", &x, &y, &z);
    if(x==y && y==z){
        printf("%d",10000+x*1000);
    }
    else if(x==y){
        printf("%d",1000+x*100);
    }
    else if(y==z){
         printf("%d",1000+y*100);
    } 
    else if(x==z){
        printf("%d",1000+z*100);
    }
    else{
        if(x>y && x>z)
                printf("%d",x*100);
        else if(y>z)
                printf("%d",y*100);
        else
           printf("%d",z*100);
    }
    return 0;
}