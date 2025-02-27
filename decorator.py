

def f1():
    print("F1 function")

f1()

def f2():
    def f3():
        print("F3 is a function")
    return f3

x = f2()
x()

def f4(f):
    def f5():
        print("Before in f5 function")
        f()
        print("After in f5 function")
    return f5

def f6():
    print("F6 function")

x = f4(f6)
print(x)

f7 = f4(f6)
f7()

