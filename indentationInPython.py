import platform

def main():
    message()

def message():
    print("Python version is {}",format(platform.python_version()))
    print("line 2")
    if True:
        print("line 3")
    else:
        print("line 4")

print("rest of code....")

if __name__== "__main__" : main()

x=43
y=75

if x<y:
    print("value of x is less than y where x is {} and y is {}".format(x,y))

