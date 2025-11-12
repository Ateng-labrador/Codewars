def capitals(word):
    res = []
    for i in range(len(word)):
        if word[i] == word[i].capitalize():
            res.append(i)
    return res
