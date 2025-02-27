def main():
    game=['rock','paper','scissors','spock','stone']
    print(game[1])
    print(game[1:3])
    print(game[1:5:2])
    game.append("Computer")
    game.insert(0,"Laptop")
    print(len(game))
    print_list(game)
    game.remove('paper')
    game.pop()
    X=game.pop(1)
    del game[3]

def print_list(o):
    for i in o:
        print(i,end=' ')
        print()

if __name__=="__main__":main()