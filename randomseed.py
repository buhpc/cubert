import sys
import random

assert(len(sys.argv) == 2)

n_steps = int(sys.argv[1])

moves = "wogrby"
appendix = ["","'","2"]

randomseed = ""
for i in range(n_steps):
    randomseed+=random.choice(moves)+random.choice(appendix)
print(randomseed)