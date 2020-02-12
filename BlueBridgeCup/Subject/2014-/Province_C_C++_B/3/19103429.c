#include<stdio.h>
int num=0;
void function(int f,int s,int sum)
{
     if(f>9 || s>5)
          return;
      if(f==9 && s==5)
      {
             if(sum==1)
             {
                 num+=1;
             }
             else
             {
                return;
             }   
      }
     function(f+1,s,sum-1);
     function(f,s+1,sum*2);
}

int main()
{
      function(0,0,2);
      printf("%d",num);
      return 0;
}
