from tkinter.font import names

import multiprocessing
import time

def worker(num):
    print(f'worker {num} started')
    time.sleep(2)
    print(f'worker {num} finished')

# if __name__ == '__main__':
    # process1 = multiprocessing.process(target = worker,arg)