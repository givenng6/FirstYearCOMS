hidden = input().upper()
guess = input().upper()

word = ''
for i in range(len(hidden)):
    if guess[i] in hidden:
        word = word + guess[i].upper()
    else:
        word = word + '.'
        
for i in range(len(word)):
    val = word[i]
    if val != '.':
        c_hidden = 0
        c_word = 0
        for c in range(len(hidden)):
            if hidden[c] == val:
                c_hidden = c_hidden + 1
            if word[c] == val:
                c_word = c_word + 1
        if c_word > c_hidden:
            index = []
            for k in range(len(hidden)):
                if word[k] == val:
                    if hidden[k] != val:
                        index.append(k)
            if len(index) > 1:
                for j in range(len(index)-1, 0, -1):
                    if c_word > c_hidden:
                        temp = word 
                        word = ''
                        for l in range(len(temp)):
                            if l == index[j]:
                                c_word = c_word - 1
                                word = word + '.'
                            else:
                                word = word + temp[l]
            else:
                for j in range(len(index)):
                    if c_word > c_hidden:
                        temp = word 
                        word = ''
                        for l in range(len(temp)):
                            if l == index[j]:
                                c_word = c_word - 1
                                word = word + '.'
                            else:
                                word = word + temp[l]
                

output = ''
for i in range(len(hidden)):
    if word[i] == hidden[i]:
        output = output + word[i]
    else:
        output = output + word[i].lower()
        
print(output)