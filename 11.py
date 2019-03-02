with open("./hightemp.txt", encoding="utf-8") as f:
    replaced = f.read().replace("\t", " ")
    with open("11.txt", mode="w", encoding="utf-8") as output:
        output.write(replaced)
