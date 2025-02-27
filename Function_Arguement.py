def main2():
    x = 5
    y =x
    print(id(x))
    print(id(y))
    display2(x)
    print(f"in main, x is {x}")

def display2(a):
    print(id(a))
    #a=3
    print(id(a))
    print("Integer is also immutable class in python")
    print(a)

main2()