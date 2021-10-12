text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

number = int(input())

result = []

for line in text:
    for word in line:
        if len(word) <= number:
            result.append(word)

print(result)
