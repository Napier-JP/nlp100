import collections
with open("hightemp.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for occurence in collections.Counter([line.split("\t")[0] for line in lines]).most_common():
        print(occurence[0], occurence[1])
'''
埼玉県 3
山形県 3
山梨県 3
群馬県 3
岐阜県 2
静岡県 2
愛知県 2
千葉県 2
高知県 1
和歌山県 1
愛媛県 1
大阪府 1
'''
