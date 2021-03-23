name = input('Hello, what is your name? \n')
print(f'Welcome {name.upper()}')
letterlist = list()
exclude = 'and'
text = input('Write out a text to form an Acronym: ')
words = text.split()
for word in words:
    if exclude.upper() and exclude.lower():
        words.remove(word)
    letter = word[0]
    letterlist.append(letter)
letters = ''.join(letterlist)
print(letters.upper())