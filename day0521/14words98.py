#O'REILLY교재 98페이지
words = ['apple', 'bat', 'bar', 'atom', 'book', 'aws', 'blue', 'cool']
by_letter = {} 

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)


print(by_letter)
print()