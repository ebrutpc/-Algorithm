#include <stdio.h>
#include <string.h>
 
void kontrolPalindrom(char [], int);
int main()
{
    char kelimePal[25];
    printf("\n\n Recursion : Girilen kelime Palindrom mu degil mi? :\n");
    printf("----------------------------------------------------------\n");
    printf(" Bir kelime giriniz : ");
    scanf("%s", kelimePal);
    kontrolPalindrom(kelimePal, 0); // kelime ve index bilgisini fonksiyona gönderir
    return 0;
}

void kontrolPalindrom(char kelimePal[],int index){

  int uzunluk = strlen(kelimePal);
  char c;
  char b;
  int s=0;
 
  c= kelimePal[index];
  b= kelimePal[uzunluk-1-index];
 
  if(c==b)
     s=1;
  
  if(index < uzunluk-1){
    kontrolPalindrom(kelimePal,index+1);
      }

  else{
    if(s==0) 
      printf("P degil");
    else
      printf("p");
                   }
  }