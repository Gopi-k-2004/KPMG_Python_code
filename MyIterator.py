class Myiterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current +=1
            return self.current -1


for i in Myiterator(1,5):
    print(i)