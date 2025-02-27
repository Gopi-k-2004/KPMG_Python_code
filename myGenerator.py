
def my_gen(start,end):
    current = start
    while current < end:
        yield current
        current +=1

for i in my_gen(10,80):
    print(i)