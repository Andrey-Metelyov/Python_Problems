word = input()
res = ""
for i in range(len(word)):
    if not word[i].islower() and i > 0:
        res += '_' + word[i].lower()
    else:
        res += word[i].lower()
print(res)
