with open("hightemp.txt", encoding="utf-8") as f:
    lines = f.readlines()
    lines.sort(key=lambda line: float(line.split("\t")[2]), reverse=True)
for line in lines:
    print(line, end="")
# 安定ソートなので変化なし
