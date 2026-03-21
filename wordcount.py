import string

text = input("Enter sentence: ").lower()

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word} : {count}")
