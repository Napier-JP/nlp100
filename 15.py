import sys

N = int(sys.argv[1])

with open("hightemp.txt", encoding="utf-8") as f:
    for line in f.readlines()[-N:]:
        print(line.rstrip())
