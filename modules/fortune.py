#!/usr/bin/env python

import os
import random

l = list()

def fortune(phenny, input):
    phenny.say(random.sample(l, 1)[0])

def load_fortune(fortune_list, file):
    fortune = ''
    f = open(file, 'r')
    for line in f:
        line = line.strip()
        if line == '%':
            fortune_list.append(fortune)
            fortune = ''
        else:
            if fortune != '':
                fortune += ' '
            fortune += line
    f.close()

fortune.commands = ['fortune']
fortune.example = '.fortune'

# Load all fortunes into memory.
files = os.listdir('fortunes')
for file in files:
    load_fortune(l, 'fortunes/' + file)

if __name__ == '__main__':
    print __doc__.strip()
