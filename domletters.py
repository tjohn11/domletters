#!/usr/bin/python3
import collections
filetext = ''
try:
    while True:
            filetext += input('')
            filetext += '\n'
except EOFError:
    words = filetext.split()
    dom_letters = 0
    invalid_chars = ['"', '.', '?', '-', ',', '\'', '!', '$']
    for word in words:
        word = word.lower()
        invalid_chars_check = list(set(word) & set(invalid_chars)) # https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
        if not invalid_chars_check:
            tupe = collections.Counter(word).most_common(1)[0] # https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
            dom_letters += tupe[1]
        else:
            continue

    print(dom_letters)