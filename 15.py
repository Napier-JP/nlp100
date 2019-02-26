import sys

N = int(sys.argv[1])

with open("hightemp.txt") as f:
    for line in f.readlines()[-N:]:
        print(line.rstrip())
