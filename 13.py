with open("13.txt", mode="w") as out:
    with open("col1.txt") as in1, open("col2.txt") as in2:
        for line1, line2 in zip(in1, in2):
            out.write(line1.rstrip() + "\t" + line2.rstrip() + "\n")
