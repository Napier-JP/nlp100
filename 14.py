import sys

with open("hightemp.txt") as f:
    for linenum, line in enumerate(f):
        if linenum >= int(sys.argv[1]):
            break
        print(line.rstrip())
