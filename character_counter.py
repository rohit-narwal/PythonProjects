# rohit - r - 1, o - 1, h - 1, i - 1, t - 1
word = input("Enter a word or paragraph: ")
words_count = {}

for char in word:
    if char in words_count:
        words_count[char] += 1
    else:
        words_count[char] = 1

print(words_count)