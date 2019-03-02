with open("./hightemp.txt", encoding="utf-8") as f:
    with open("col1.txt", mode="w", encoding="utf-8") as col1_out, open("col2.txt", mode="w", encoding="utf-8") as col2_out:
        for line in f:
            cols = line.split("\t")
            col1_out.write(cols[0] + "\n")
            col2_out.write(cols[1] + "\n")
