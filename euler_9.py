a = 207
b = 224
c = 305

result=0

while(a+b+c < 1000):
    a +=1
    b +=1
    c +=1
    result = a**2 + b**2 - c**2
    if(result==0):
        print(a,b,c)

        
