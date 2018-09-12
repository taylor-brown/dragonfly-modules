key_combos = {
    'pad': ('down:25'),
    'pug': ('up:25'),
    'home': ('home'),
    'feen': ('end'),
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
    'sentence <text>': ('%(text)s'),
    'proper <text>': ('%(text)s'),
    'camel <text>': ('%(text)s'),
    'path <text>': ('%(text)s'),
    'score <text>': ('%(text)s'),
    'jumble <text>' :('%(text)s'),
    'dashword <text>': ('%(text)s'),
    'capword <text>': ('%(text)s'),
    'dotword <text>': ('%(text)s'),
    'natword <text>': ('%(text)s'),
}

symbols = {
    "amp": "ampersand",
    "ash": "slash",
    "atsign": "at",
    "backash": "backslash",
    "backtick": "backtick",
    "bang": "exclamation",
    "langle": "lessthan",
    "rangle": "greaterthan",
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
    "sol": "asterisk",
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

tokens = map(lambda x: x.upper(),
             ['key_combos', 'multiples', 'symbols', 'Alpha', 'num'] + map(lambda m: m.split(' ')[0], texts.keys()))

all_keys = {}
all_keys.update(simple_keys)
all_keys.update(texts)

# Ignored characters
t_ignore = " 	"

t_KEY_COMBOS = '|'.join(key_combos.keys())
t_MULTIPLES = '|'.join(multiples.keys())
t_SYMBOLS = '|'.join(symbols.keys())
t_ALPHA = '|'.join(alpha.keys())
t_NUM = '|'.join(num.keys())


def t_SENTENCE(t):
    r'sentence .*'#feen'
    t.value = t.value[9:]
    t.value = t.value.capitalize()
    return t


def t_CAPWORD(t):
    r'capword .*'#feen'
    t.value = t.value[8:]
    t.value = t.value.upper()
    return t


def t_DASHWORD(t):
    r'dashword .*'#feen'
    t.value = t.value[9:]
    t.value = '-'.join(t.value.split(' '))
    return t


def t_PROPER(t):
    r'proper .*'#feen'
    t.value = t.value[7:]
    t.value = ''.join([i.capitalize() for i in t.value.split(' ')])
    return t


def t_CAMEL(t):
    r'camel .*'#feen'
    t.value = t.value[6:]

    def format_camel(text):
        return text[0].lower() + ''.join([word[0].upper() + word[1:] for word in text[1:]])

    t.value = format_camel(t.value.split(' '))
    return t


def t_PATH(t):
    r'path .*'#feen'
    t.value = t.value[5:]
    t.value = '/'.join(t.value.split(' '))
    return t


def t_SCORE(t):
    r'score .*'#feen'
    t.value = t.value[6:]
    t.value = '_'.join(t.value.split(' '))
    return t


def t_JUMBLE(t):
    r'jumble .*'#feen'
    t.value = t.value[7:]
    t.value = ''.join(t.value.split(' '))
    return t


def t_DOTWORD(t):
    r'dotword .*'#feen'
    t.value = t.value[8:]
    t.value = '.'.join(t.value.split(' '))
    return t


def t_NATWORD(t):
    r'natword .*'#feen'
    t.value = t.value[8:]
    return t


from dragonfly import Key, Text
# class Text(object):
#     def __init__(self, txt):
#         self.txt = txt
#         super(Text, self).__init__()
#
#     def __repr__(self):
#         return 'Text:' + self.txt
#
#
# class Key(object):
#     def __init__(self, txt):
#         self.txt = txt
#         super(Key, self).__init__()
#
#     def __repr__(self):
#         return "key:" + self.txt


def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]


def p_expr_expr(t):
    'expression : expression expression'
    t[0] = t[1] + t[2]


def p_number(t):
    """number : NUM
    """
    ints = {'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'niner': '9', }

    t[0] = ints[t[1]]


def p_key(t):
    """expression : KEY_COMBOS
                    | SYMBOLS

 """
    t[0] = [Key(all_keys[t[1]])]


def p_text_expression(t):
    """expression : SENTENCE
                 | PROPER
                 | CAMEL
                 | PATH
                 | SCORE
                 | JUMBLE
                 | DOTWORD
                 | NATWORD
                 | CAPWORD
                 | DASHWORD
    """
    t[0] = [Text(t[1])]


def p_keytext_expression(t):
    """expression : ALPHA

    """
    t[0] = [Text(all_keys[t[1]])]


def p_expression_number(t):
    """expression : number"""
    t[0] = [Text(t[1])]


def p_multiple(t):
    """multiple : MULTIPLES"""
    t[0] = Key(multiples[t[1]])


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

yacc.yacc(debugfile=r'\tmp\parser.out', outputdir='\\tmp\\', write_tables=False)
ext_yacc = yacc

# print yacc.parse("alpha proper roads are going through here stuff")