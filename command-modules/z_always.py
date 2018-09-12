# This is a command module for Dragonfly. It provides bindings for the Linux
# window manager always. Only active when running via proxy and the server
# reports Linux.

# You may find this useful to disable the Windows key in windows stealing focus
# from the client.
# http://support.microsoft.com/kb/216893#LetMeFixItMyselfAlways

print 'importing always'
import dragonfly

import lex_parse

grammar = dragonfly.Grammar('always')

from dragonfly import *


def textify(input):
    for x in input:
        input[x] = Text(input[x])


class Compound(CompoundRule):
    f=open('/tmp/log.txt', "a")
    inner_keys = '( ' + '|'.join(lex_parse.all_keys.keys()) + ')'
    spec = inner_keys + ('[' + inner_keys + ']') * 30
    extras = [aenea.misc.DigitalInteger('n', 1, None), Dictation(name='text')]
    defaults = {
        'n': 1,
        }

    def _process_recognition(self, value, extras):
        words = ' '.join(map(lambda x:x.split('\\')[0], value.words()))
        self.f.write(words+"\n")
        self.f.flush()
        [i.execute() for i in lex_parse.ext_yacc.parse(words)]


grammar.add_rule(Compound())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
