import time
import random

fs = set()


def write(file):
    print(f'start writing {file} to fs')
    time.sleep(2 * random.random())
    fs.add(file)
    print(f'{file} written to fs')
    print('fs state:', fs)

def exists(file):
    return file in fs
