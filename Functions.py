def greet_user(name):
    print(f"Hello, {name}! welcome to python")

greet_user("ABC")

def add(a,b):
    return a+b

def isOdd(a):
    if a%2==0:
        return "even"
    else:
        return "Odd"

result = add(10,12)
print("result is {}".format(result))

x = isOdd(5)
print("x is {}".format(x))

from math import sqrt, pi

print(sqrt(20))

import random
from datetime import datetime

fruits = ['apple','orange','papaya']
print(random.randint(1,100))
print(random.choice(fruits))
print(datetime.now())

def greet(name,message = "Hello"):
    print(f"{message},{name}!")

greet(name = "ABC",message="Hi")
greet(name = "ABC2")

def sum_all(*args):
    return sum(args)

sum_all(1,2,3,4)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_info(name = "ABC",age = 25)