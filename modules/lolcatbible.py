#!/usr/bin/env python

import os
import random

l = list()

def lolcatbible(phenny, input):
    phenny.say(random.sample(l, 1)[0])

def load_bible(bible_list, file, book):
    f = open(file, 'r')
    for line in f:
        line = line.strip()
        bible_list.append(book + ':' + line)
    f.close()

lolcatbible.commands = ['lolcatbible']
lolcatbible.example = '.lolcatbible'

files = os.listdir('lolcatbible')
for file in files:
    load_bible(l, 'lolcatbible/' + file, file)

if __name__ == '__main__':
    print __doc__.strip()
