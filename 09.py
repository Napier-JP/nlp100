import random
s = "I couldn't believe that I could actually understand what I was reading: the phenomenal power of the human mind ."
words = s.split()


def scramble(word):
    if len(word) > 4:
        return word[0] + "".join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
    else:
        return word


print(" ".join([scramble(word) for word in words]))
# I c'dunolt bvleiee that I cloud allucaty urtasndend what I was raingde: the pmnaoeenhl peowr of the hamun mind .
# ちょっと読めませんねえ
