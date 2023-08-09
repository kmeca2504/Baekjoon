#include <stdio.h>

int main(){
    int x,y,z;
    scanf("%d", &z);
    for(int i=0; i<z; i++){
        scanf("%d %d", &x, &y);
        printf("%d\n",x+y);
    }
    return 0;
}