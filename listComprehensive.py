from math import pi

def main():
    seq = range(11)
    seq1 = [x*2 for x in seq]
    seq2 = [x for x in seq if x%2 !=0]
    seq3 = [(x,x**2) for x in seq]
    seq4 = [round(pi,i) for i in seq]
    seq5 = {x:x**3 for x in seq} # dictionary


    print_list(seq5.items())

def print_list(o):
    for x in o:
        print(x,end = " ")
        print()

if __name__ == '__main__' : main()
