#include <stdio.h>

int main() {
	int a, b;
	int fir, sec, thi;
	
	scanf("%d %d", &a, &b);
	fir = b % 10;
	sec = (b / 10) % 10;
	thi = b / 100;
	printf("%d\n%d\n%d\n%d",a*fir, a*sec, a*thi , b * a);

	return 0;

}