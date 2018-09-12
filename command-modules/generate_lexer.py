key_combos = {
    'pad': ('down:25'),
    'pug': ('up:25'),
    'home': ('home'),
    'end': ('end'),
    'whoops': ('c-z'),
    'reoops': ('cs-z'),
    'copy': ('c-c'),
    'cut': ('c-x'),
    'paste': ('c-v'),

    'filetop': 'c-home',
    'filetoe': ('c-end'),
    'comment': ('c-slash')

}

multiples = {
    'up': ('up'),
    'down': ('down'),
    'left': ('left'),
    'right': ('right'),
    'lope': ('c-left'),
    'rope': ('c-right'),
    'srope': ('cs-right'),
    'slope': ('cs-left'),
    'ace': ('space'),
    'act': ('escape'),
    'chuck': ('del'),
    'scratch': ('backspace'),
    'slap': ('enter'),
    'tab': ('tab'),
    'bump': ('c-del'),
    'whack': ('c-backspace'),
    "seedown": ("shift:down, down,shift:up"),
    "seeup": ("shift:down, up,shift:up"),

}

texts = {
    'sentence <text> feen': ('%(text)s'),
    'proper <text> feen': ('%(text)s'),
    'camel <text> feen': ('%(text)s'),
    'path <text> feen': ('%(text)s'),
    'score <text> feen': ('%(text)s'),
    'jumble <text> feen': ('%(text)s'),
    'dashword <text> feen': ('%(text)s'),
    'dotword <text> feen': ('%(text)s'),
    'natword <text> feen': ('%(text)s'),
}

symbols = {
    "amp": "ampersand",
    "ash": "slash",
    "atsign": "at",
    "backash": "backslash",
    "backtick": "backtick",
    "bang": "bang",
    "bar": "bar",
    "dollar": "dollar",
    "dot": "dot",
    "drip": "comma",
    "eek": "equal",
    "hat": "caret",
    "hyph": "minus",
    "percent": "percent",
    "pop": "rparen",
    "pound": "hash",
    "push": "lparen",
    "quest": "question",
    "quote": "dquote",
    "rail": "underscore",
    "semi": "semicolon",
    "smote": "squote",
    "sol": "star",
    "tilde": "tilde",
    "yeah": "colon",

    "bitore": "bar",
    "bitand": "and",
    "bitexor": "caret",
    "divided": "slash",
    "plus": "plus",
    "minus": "minus",
    'boxso': 'lbrace',
    'boxco': 'rbrace',
    'squareso': 'lbracket',
    'squareco': 'rbracket'

}

num = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'niner': '9',
}
alpha = {
    "capuncle": "U"
    , "capnuts": "N"
    , "capitem": "I"
    , "capjohnny": "J"
    , "caplove": "L"
    , "capsugar": "S"
    , "caproger": "R"

    , "uncle": "u"
    , "nuts": "n"
    , "item": "i"
    , "johnny": "j"
    , "love": "l"
    , "sugar": "s"
    , "roger": "r"
    ,
    'capalpha': 'A',
    'capbravo': 'B',
    'capcharlie': 'C',
    'capdelta': 'D',
    'capecho': 'E',
    'capfoxtrot': 'F',
    'capgolf': 'G',
    'caphotel': 'H',
    'capkilo': 'K',
    'capmike': 'M',
    'caposcar': 'O',
    'cappoppa': 'P',
    'capquiche': 'Q',
    'captango': 'T',
    'capvictor': 'V',
    'capwhiskey': 'W',
    'capxray': 'X',
    'capyankee': 'Y',
    'capzulu': 'Z',

    'alpha': 'a',
    'bravo': 'b',
    'charlie': 'c',
    'delta': 'd',
    'echo': 'e',
    'foxtrot': 'f',
    'golf': 'g',
    'hotel': 'h',
    'kilo': 'k',
    'mike': 'm',
    'oscar': 'o',
    'poppa': 'p',
    'quiche': 'q',
    'tango': 't',
    'victor': 'v',
    'whiskey': 'w',
    'xray': 'x',
    'yankee': 'y',
    'zulu': 'z',

}

simple_keys = {}
simple_keys.update(key_combos)
simple_keys.update(multiples)
simple_keys.update(symbols)
simple_keys.update(alpha)
simple_keys.update(num)

tokens = simple_keys.keys()

token_list = []

all_keys = {}
all_keys.update(simple_keys)
all_keys.update(texts)

defs = '''

# Ignored characters
t_ignore = " \t"

def t_SENTENCE(t):
    r'sentence .*? feen'
    t.value = t.value[9:-5]
    t.value = t.value.capitalize()
    return t


def t_PROPER(t):
    r'proper .*? feen'
    t.value = t.value[7:-5]
    t.value = ''.join([i.capitalize() for i in t.value.split(' ')])
    return t


def t_CAMEL(t):
    r'camel .*? feen'
    t.value = t.value[4:-5]
    def format_camel(text):
        return text[0] + ''.join([word[0].upper() + word[1:] for word in text[1:]])

    t.value = format_camel(t.value.split(' '))
    return t

def t_PATH(t):
    r'path .*? feen'
    t.value = t.value[5:-5]
    t.value = '/'.join(t.value.split(' '))
    return t

def t_SCORE(t):
    r'score .*? feen'
    t.value = t.value[6:-5]
    t.value = '_'.join(t.value.split(' '))
    return t


def t_JUMBLE(t):
    r'jumble .*? feen'
    t.value = t.value[7:-5]
    t.value = ''.join(t.value.split(' '))
    return t


def t_DOTWORD(t):
    r'dotword .*? feen'
    t.value = t.value[8:-5]
    t.value = '.'.join(t.value.split(' '))
    return t


def t_NATWORD(t):
    r'natword .*? feen'
    t.value = t.value[7:-5]
    return t
'''

def print_bar(tin):
    print '\n | '.join([n.replace(' ','_').upper() for n in sorted(tin.keys())])

# print_bar(key_combos)
# print_bar(multiples)
# print_bar(symbols)
# print_bar(alpha)

parsers = '''
from aenea.lax import Key, Text

def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]

def p_expr_expr(t):
    'expression : expression expression'
    t[0] = t[1] + t[2]


def p_number(t):
    """number : EIGHT
             | FIVE
             | FOUR
             | NINER
             | ONE
             | SEVEN
             | SIX
             | THREE
             | TWO
             | ZERO

    """
    ints = {    'zero':'0',
    'one':'1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'niner': '9',}

    t[0] = ints[t[1]]

def p_key(t):
    """expression : COPY
                 | COMMENT
                 | END
                 | FILETOE
                 | FILETOP
                 | HOME
                 | PAD
                 | PASTE
                 | PUG
                 | REOOPS
                 | WHOOPS

 """
    t[0] = [Key(generate_lexer.all_keys[t[1]])]

def p_text_expression(t):
    """expression : SENTENCE
                 | PROPER
                 | CAMEL
                 | PATH
                 | SCORE
                 | JUMBLE
                 | DOTWORD
                 | NATWORD
    """
    t[0] = [Text(t[1])]

def p_keytext_expression(t):
    """expression : AMP
                 | ASH
                 | AT_SIGN
                 | BACK_ASH
                 | BACKTICK
                 | BANG
                 | BAR
                 | BIT_AND
                 | BIT_EX_OR
                 | BIT_ORE
                 | BOXCO
                 | BOXSO
                 | DIVIDED
                 | DOLLAR
                 | DOT
                 | DRIP
                 | EEK
                 | HAT
                 | HYPH
                 | MINUS
                 | PERCENT
                 | PLUS
                 | POP
                 | POUND
                 | PUSH
                 | QUEST
                 | QUOTE
                 | RAIL
                 | SEMI
                 | SMOTE
                 | SQUARECO
                 | SQUARESO
                 | STAR
                 | TILDE
                 | YEAH
                 | ALPHA
                 | BRAVO
                 | CHARLIE
                 | DELTA
                 | ECHO
                 | FOXTROT
                 | GOLF
                 | HOTEL
                 | ITEM
                 | JOHNNY
                 | KILO
                 | LOVE
                 | MIKE
                 | NUTS
                 | OSCAR
                 | POPPA
                 | QUICHE
                 | ROGER
                 | SUGAR
                 | TANGO
                 | UNCLE
                 | CAP_ALPHA
                 | CAP_BRAVO
                 | CAP_CHARLIE
                 | CAP_DELTA
                 | CAP_ECHO
                 | CAP_FOXTROT
                 | CAP_GOLF
                 | CAP_HOTEL
                 | CAP_ITEM
                 | CAP_JOHNNY
                 | CAP_KILO
                 | CAP_LOVE
                 | CAP_MIKE
                 | CAP_NUTS
                 | CAP_OSCAR
                 | CAP_POPPA
                 | CAP_QUICHE
                 | CAP_ROGER
                 | CAP_SUGAR
                 | CAP_TANGO
                 | CAP_UNCLE
                 | CAP_VICTOR
                 | CAP_WHISKEY
                 | CAP_XRAY
                 | CAP_YANKEE
                 | CAP_ZULU
                 | VICTOR
                 | WHISKEY
                 | XRAY
                 | YANKEE
                 | ZULU
    """
    t[0] = [Text(generate_lexer.all_keys[t[1]])]

def p_expression_number(t):
    """expression : number"""
    t[0] = [Text(t[1])]

def p_multiple(t):
    """multiple : ACE
                 | ACT
                 | BUMP
                 | CHUCK
                 | DOWN
                 | LEFT
                 | LOPE
                 | RIGHT
                 | ROPE
                 | SEEUP
                 | SEEDOWN
                 | SCRATCH
                 | SLAP
                 | SLOPE
                 | SROPE
                 | TAB
                 | UP
                 | WHACK"""
    t[0] = Key(generate_lexer.multiples[t[1]])

def p_expression_multiple(t):
    """ expression : multiple
                    | multiple number"""
    p = []
    if len(t) > 2:
        p = [t[1]] * int(t[2])
    else:
        p = [t[1]]
    t[0] = p

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_error(t):
    print("Syntax error at '%s'" % t)

import ply.lex as lex
lex.lex()

import ply.yacc as yacc
yacc.yacc()
ext_yacc = yacc
'''
if __name__ == "__main__":
    print parsers
    for token in sorted(tokens):
        t = token.upper().replace(' ', '_')
        token_list.append(t)
        print 't_' + t + ' = r"' + token + '"'

    print 'tokens = ', token_list + ['SENTENCE',
                                     'PROPER',
                                     'CAMEL',
                                     'PATH',
                                     'SCORE',
                                     'JUMBLE',
                                     'DOTWORD',
                                     'NATWORD']
    print defs

