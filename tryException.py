
def main():
    try:
        s = int('abc')
    except ValueError:
        print('value error caught')

print('rest of code')

if __name__ == '__main__' : main()

def main2():
    try:
        x = 3/4
    except ValueError:
        print("Value error")
    except ZeroDivisionError:
        print("dont divide a number by 0")
    else:
        print("code ran successfully value of x is ",x)

if __name__ == '__main__': main2()
