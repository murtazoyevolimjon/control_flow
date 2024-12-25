text = input("Matnni kiriting: ")#birorta matn kiriting

words = text.split()
max_word = text[0]

long_word = max(words, key=len)
print("Eng uzun so'z:", long_word)

for word in words:
    if len(word) > len(max_word):
        max_word = word

print("Eng uzun so'z:", max_word)
