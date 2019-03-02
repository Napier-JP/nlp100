with open("13.txt", mode="w", encoding="utf-8") as out:
    with open("col1.txt", encoding="utf-8") as in1, open("col2.txt", encoding="utf-8") as in2:
        for line1, line2 in zip(in1, in2):
            out.write(line1.rstrip() + "\t" + line2.rstrip() + "\n")
