words = []
word = input().upper()

while(word != '###'):
    words.append(word)
    word = input().upper()

size = len(words)
print(size)