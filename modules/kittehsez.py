#!/usr/bin/env python

import sys

def kittehsez(phenny, input):
    phenny.say('.       .  . o O( %s )' % input.group(2))
    phenny.say('\`-"\'"-\'/')
    phenny.say(' } 6 6 {')
    phenny.say('=.  Y  ,=')
    phenny.say('  /^^^\  .')
    phenny.say(' /     \  )')
    phenny.say('(  )-(  )/')
    phenny.say(' ""   ""')

kittehsez.commands = ['kittehsez']
kittehsez.example = '.kittehsez'

if __name__ == '__main__':
    print __doc__.strip()
