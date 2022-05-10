hidden = input().upper()
guess = input().upper()

word = ''
for i in range(len(hidden)):
    if guess[i] in hidden:
        if hidden[i] == guess[i]:
            word = word + guess[i].upper()
        else:
            word = word + guess[i].lower()
    else:
        word = word + '.'

print(word)