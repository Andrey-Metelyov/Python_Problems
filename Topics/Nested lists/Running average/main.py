digits = [int(x) for x in input()]
# digits = [int(x) for x in list("12345")]
moving_average = [(digits[i] + digits[i + 1]) / 2 for i in range(0, len(digits) - 1)]

print(moving_average)
