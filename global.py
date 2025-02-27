from traceback import print_list

dlevel =0

def main():
    r = range(11)
    l = [1,"two",3,{'4':'four'},5]
    t = ['one','two','three','four','five']
    s = set("list comprehension is a powerful termination for creating list/data structure or other collections")
    d = dict(one =r,two = l,three=t)
    mixed = [l,r,t,s,d]

def display(o):
    global dlevel

    dlevel +=1
    if isinstance(o,list) : print_list(o)
    elif isinstance(o,range) : print_range(o)
    elif isinstance(o, tuple): print_tuple(o)
    elif isinstance(o, set): print_set(o)
    elif isinstance(o, dict): print_dict(o)
    elif o is None : print("No DS",end = ' ')
    else: print(repr(o),end = ' ')
    dlevel -= 1

    if dlevel <=1 : print()

def print_list(o):
    print('[',end = ' ')
    for x in o : display(x)
    print(']',end = '')


def print_tuple(o):
    print('(',end = ' ')
    for x in o : display(x)
    print(')',end = '')

def print_set(o):
    print('{',end = ' ')
    for x in o : display(x)
    print('}',end = '')

def print_dict(o):
    print('{',end=' ')
    for x,y in o.items():
        print(x,end=' ')
        display(x)
    print('}',end='')

if __name__ == '__main__' : main()