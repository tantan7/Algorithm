#include <stdio.h>
int f(int n)
{
    int f=0;
    int a[5];
    for(int i=0;i<5;i++)
    {
        a[i] = n % 10;
        if (a[i] == 4)
        {
            f=1;
        }
        n = n / 10;
    }
    return f;
}
int main()
{
    int sum=900000;
    for(int i=10000;i<100000;i++)
    {
        sum=sum-f(i);
    }
    printf("%d",sum);
}
