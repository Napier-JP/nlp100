import sys

N = int(sys.argv[1])

with open("hightemp.txt", encoding="utf-8") as f:
    lines = list(map(lambda l: l.rstrip("\n"), f.readlines()))
    step = -(-len(lines) // N)  # equivalent to math.ceiling but faster
    for i in range(1, N + 1):
        with open("split_{}".format(i), mode="w", encoding="utf-8") as out:
            out.write("\n".join(lines[step * (i - 1):step * i]))
