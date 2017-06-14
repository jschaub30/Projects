#!/usr/bin/env python3

# https://github.com/karan/Projects

def happy(num, history=[]):
    #print('Happy of {}'.format(num))
    if num in history:
        #history.append(num)
        #print(history)
        return False
    history.append(num)
    if num == 1:
        return True
    else:
        return happy(sum([int(digit) ** 2 for digit in str(num)]), history)

count = 0
num = 1
while count < 10:
    if happy(num, history=[]):
        print("{} is happy".format(num))
        count += 1
    num += 1


