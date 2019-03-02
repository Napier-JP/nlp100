s1 = "paraparaparadise"
s2 = "paragraph"


def n_gram(n, arg_iterable):
    return [arg_iterable[i:i + n] for i in range(len(arg_iterable) - n + 1)]


X = set(n_gram(2, s1))
Y = set(n_gram(2, s2))

print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)
'''
{'ar', 'gr', 'is', 'di', 'ag', 'ad', 'se', 'pa', 'ap', 'ph', 'ra'}
{'pa', 'ap', 'ar', 'ra'}
{'is', 'di', 'ad', 'se'}
True
False
'''
