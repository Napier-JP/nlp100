with open("./hightemp.txt") as f:
    replaced = f.read().replace("\t", " ")
    with open("11.txt", mode="w") as output:
        output.write(replaced)
