words = []
word = input().upper()

while(word != '###'):
    words.append(word)
    word = input().upper()
    
guess = input().upper()

if len(guess) == 5:
    if guess in words:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
