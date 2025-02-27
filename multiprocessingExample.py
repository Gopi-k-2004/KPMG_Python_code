import multiprocessing
import time

def square(x):
    return x * x

#added comment for github

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(11))

    print(results)
