hidden = input().upper()
guess = input().upper()

counter = 0
for i in range(len(hidden)):
    if guess[i] == hidden[i]:
        counter = counter + 1
        
print(counter)
