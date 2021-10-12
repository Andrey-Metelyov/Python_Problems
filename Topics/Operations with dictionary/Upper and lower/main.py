# the list with words from string
# please, do not modify it
some_iterable = input().split()
# some_iterable = "Great loves too must be endured.".split()

# use dictionary comprehension to create a new dictionary
new_dict = {word.upper(): word.lower() for word in some_iterable}

print(new_dict)
