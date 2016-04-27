# Fatto da Davide Barbini

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def codifica(alfab, key=0, word=""):
    out_word = ""
    for letter in word:
        index = alfab.index(letter) - (len(alfab)-key)
        out_word += alfab[index]

    return out_word

print(codifica(alfabeto, 5, "wjgjbiv"))
