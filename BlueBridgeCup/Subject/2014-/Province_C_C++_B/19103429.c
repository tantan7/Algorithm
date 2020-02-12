#include<stdio.h>
int main()
{
    int p,y;
       for(p=0;p<36;p++)
       {
            for(y=0;p<43;y++)
            {
                  if(p*2.3+y*1.9==82.3  && p<y)
                  {printf("%d",p);}
            }
       }
return 0;
}
