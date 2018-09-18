#import <stdio.h>
#import <math.h>
int main()
{
  int primes[2000001];
  for (int i=0; i<=2000000; i++)
  {
    primes[i]=1;
  }
  primes[0]=0;
  primes[1]=0;

  for(int i=2; i<=1415; i++)
  {
    if(primes[i]==1)
    {
      for(int j=2;i*j<=2000000; j++)
      {
        primes[i*j]=0;
      }
    }
  }
}
