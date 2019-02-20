s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = s.split(" ")
ans = []


def isalpha(x):
    return x.isalpha()


for word in words:
    ans.append(len(list(filter(isalpha, word))))

print(ans)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
