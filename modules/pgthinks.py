#!/usr/bin/env python

import sys

def pgthinks(phenny, input):
    phenny.say('          __     __')
    phenny.say('         /  \\~~~/  \\  . o O ( %s ) ' %input.group(2))
    phenny.say('   ,----(     oo    )')
    phenny.say('  /      \\__     __/')
    phenny.say(' /|         (\\  |(')
    phenny.say('^ \\   /___\\  /\\ |')
    phenny.say('   |__|   |__|-"')


pgthinks.commands = ['pgthinks']
pgthinks.example = '.pgthinks'

if __name__ == '__main__':
    print __doc__.strip()
