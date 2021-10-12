def translate(**words):
    # print(words)
    for (word1, word2) in words.items():
        print(word1, ":", word2)

words = {"mother": "madre", "father": "padre", 
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
