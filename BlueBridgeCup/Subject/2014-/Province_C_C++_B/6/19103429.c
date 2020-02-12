#include<stdio.h>
int main()
{
      int a,b,c,d;
      int sum=0;
      for(a=1;a<10;a++)
      {   
            for(b=1;b<10;b++)
            {
                   if(a != b)
                   { 
                        for(c=1;c<10;c++)
                        {
                             for(d=1;d<10;d++)
                             {
                                  if(c != d)
                                  {
                                        if((10*a+c)*b*d == (10*b+d)*a*c)
                                               sum+=1;
                                  }
                             }
                        }
                   }
            }
      }
      printf("%d",sum);
return 0;
}
