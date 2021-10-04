string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print(count)
