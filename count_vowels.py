#!/usr/bin/env python3

# https://github.com/karan/Projects

import collections
def count_vowels(text):
    ''' count all vowels in text '''
    count = collections.Counter(text.lower())
    return (text, sum([count[x] for x in count if x in 'aeiou']))

print(count_vowels('aeidd'))  #3
print(count_vowels('ABCDE'))  #2

