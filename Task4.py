hidden = input().upper()
guess = input().upper()
li = []

counter = 0
for i in range(len(hidden)):
    if guess[i] == hidden[i]:
        counter = counter + 1
    else:
        li.append(guess[i])
        
count = 0
for i in range(len(li)):
    if li[i] in hidden:
        count = count + 1
        
        
        
print(counter)
print(count)