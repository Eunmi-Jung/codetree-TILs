#include <stdio.h>
#include<string.h>

int main() {
    char str[5][10]={"apple", "banana", "grape", "blueberry", "orange"};
    char c,*p;
    int i,n,cnt=0;
    scanf("%c",&c);
    for(i=0;i<5;i++)
    {
      p=strchr(str[i]+2,c);
      if(p-str[i]==2 ||p-str[i]==3){
      printf("%s\n",str[i]);
      cnt++;
      }
    }
    printf("%d",cnt);
    return 0;
}