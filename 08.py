s = "In CONGRESS, July 4, 1776. The unanimous Declaration of the thirteen united States of America"


def cipher(original_text):
    processed = ""
    for char in original_text:
        if char.islower():
            processed += chr(219 - ord(char))
        else:
            processed += char
    return processed


print(cipher(s))
print(cipher(cipher(s)))
'''
Im CONGRESS, Jfob 4, 1776. Tsv fmzmrnlfh Dvxozizgrlm lu gsv gsrigvvm fmrgvw Sgzgvh lu Anvirxz
In CONGRESS, July 4, 1776. The unanimous Declaration of the thirteen united States of America
'''
