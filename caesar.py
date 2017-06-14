#!/usr/bin/env python3

# https://github.com/karan/Projects

#### Caesar cypher
import string

def convert(letter, key):
    assert len(letter) == 1
    if letter not in string.ascii_lowercase:
        return letter
    idx = (string.ascii_lowercase.index(letter.lower()) + key ) % 26
    new_letter = string.ascii_lowercase[idx]
    if letter.isupper():
        return new_letter.upper()
    return new_letter

def caesar(phrase, key, decode=False):
    '''Caesar cipher'''
    assert 0 < key < 26
    if decode:
        key = -key
    return ''.join([convert(letter, key) for letter in phrase])

code = caesar('The quick brown fox', 1)
decode = caesar(code, 1, decode=True)
print(code)
print(decode)

