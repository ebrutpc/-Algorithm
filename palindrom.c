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
  char c[25];
  char b[25];
  int s=0;
 
  c[index]= kelimePal[index];
  b[index]= kelimePal[uzunluk-1-index];
  //printf("c:%c b:%c\n ",c[index],b[index]);
  //printf("index:%d\n ",index);
  if(c[index]==b[index])
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
 
   
 