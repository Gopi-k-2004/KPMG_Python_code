class Duck:
    var1 = 'quaack'
    var2 = 'walks like a Duck!'

    def quack(self):
        print(self.var1)

    def walk(self):
        print(self.var2)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__' : main()