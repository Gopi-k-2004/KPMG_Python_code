words = ['One','Two','Three','Four','Five'] # in python strings are immutable

# [] means list also immutable
n =0
while(n<5):
    print(words[n],end = " ")
    n +=1

for i in words:
    print(i,end = " ")

a,b =0,1
while b < 1000:
    print(b,end = " ")
    a,b=b,a+b

print()