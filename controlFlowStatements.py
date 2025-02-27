x = 10

if x > 5:
    print("x is greater than 5")
    print("value of x = ",format(x) + " is greater than 5")
    # print(f"value of x = ",{x}+"greater than 5")

import platform # this is how we load module or library in python

version = platform.python_version()

print('python Version on my system is {}'.format(platform.python_version()));

def main():
    print(f' py version is {version}')


if __name__=='__main__': main()  # first function to be callede by the compiler


