#include <stdio.h>
int n,m,k;
int sum = 0;
int arr[50][50];
void f(int x,int y,int num,int max)
{
   if(x>n || y>m || num>k) return;
   else{
       if(x==n-1 && y==m-1)
       {
           if(num==k)
           {
               sum=(sum+1)%1000000007;
           }
           if(num==k-1 && arr[x][y]>max)
           {
               sum=(sum+1)%1000000007;
           }
       }
       else{
           if(arr[x][y]>max) {
               f(x + 1, y, num + 1, arr[x][y]);
               f(x, y + 1, num + 1, arr[x][y]);
           }
       }
       f(x + 1,y,num,max);
       f(x,y + 1,num,max);
   }

}
int main() {
    scanf("%d",&n);
    scanf("%d",&m);
    scanf("%d",&k);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
   f(0,0,0,0);
   printf("%d",sum);
   return 0;
}
