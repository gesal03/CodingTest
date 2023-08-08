#include <stdio.h>
#define SIZE 1000000

int main() {
 	int n;
	scanf("%d",&n);
	
	int arr[SIZE]={0};
	
	int a,b;
	for(int i=0;i<n;i++){
		scanf("%d %d",&a,&b);
		arr[i] =a+b;
	}
	for(int i=0;i<n;i++){
		printf("%d\n",arr[i]);
	}
}