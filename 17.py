with open("hightemp.txt", encoding="utf-8") as f:
    prefs = set()
    for line in f:
        prefs.add(line.split("\t")[0])
    print(prefs)
# {'山梨県', '埼玉県', '和歌山県', '高知県', '群馬県', '千葉県', '岐阜県', '愛媛県', '静岡県', '山形県', '大阪府', '愛知県'}
