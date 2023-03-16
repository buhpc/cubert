import sys
import random

def getrandomseed(n_steps):

    moves = "wogrby"
    appendix = ["","'","2"]

    randomseed = ""
    for i in range(n_steps):
        randomseed+=random.choice(moves)+random.choice(appendix)
    return randomseed

if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    n_steps = int(sys.argv[1])
    print(getrandomseed(n_steps))