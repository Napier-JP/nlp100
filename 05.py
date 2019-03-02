s = "I am an NLPer"


def n_gram(n, arg_iterable):
    return [arg_iterable[i:i + n] for i in range(len(arg_iterable) - n + 1)]


word_bigram = n_gram(2, s.split())
print(word_bigram)
# [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]

char_bigram = n_gram(2, s)
print(char_bigram)
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
