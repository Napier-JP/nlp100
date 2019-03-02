with open("./hightemp.txt") as f:
    with open("col1.txt", mode="w") as col1_out, open("col2.txt", mode="w") as col2_out:
        for line in f:
            cols = line.split("\t")
            col1_out.write(cols[0] + "\n")
            col2_out.write(cols[1] + "\n")
