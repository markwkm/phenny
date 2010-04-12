#!/usr/bin/env python

import sys

def mythinks(phenny, input):
    phenny.say('      ,-._')
    phenny.say('    _.-\'  \'--. . o O ( %s ) ' %input.group(2))
    phenny.say('  .\'      _  o`\\_')
    phenny.say(' / .----.`_.\'----\'')
    phenny.say(' ;/     `')
    phenny.say('/_;')


mythinks.commands = ['mythinks']
mythinks.example = '.mythinks'

if __name__ == '__main__':
    print __doc__.strip()
