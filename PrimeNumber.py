from math import sqrt

def isprime(n):
    if n<=1 :
        return False
    for x in range(2,int(sqrt(n))+1):
        if(n%x ==0):
            return False
    return True



# n = 5
# if isprime(n):
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')

def list_prime():
    for n in range(100):
        if isprime(n):
            print(n,end = " ")
    print()

list_prime()