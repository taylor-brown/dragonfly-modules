#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

"""
Command-module for cursor movement and **editing**
============================================================================

This module allows the user to control the cursor and 
efficiently perform multiple text editing actions within a 
single phrase.


Example commands
----------------------------------------------------------------------------

*Note the "/" characters in the examples below are simply 
to help the reader see the different parts of each voice 
command.  They are not present in the actual command and 
should not be spoken.*

Example: **"up 4 / down 1 page / home / space 2"**
   This command will move the cursor up 4 lines, down 1 page,
   move to the beginning of the line, and then insert 2 spaces.

Example: **"left 7 words / backspace 3 / insert hello Cap world"**
   This command will move the cursor left 7 words, then delete
   the 3 characters before the cursor, and finally insert
   the text "hello World".

Example: **"home / space 4 / down / 43 times"**
   This command will insert 4 spaces at the beginning of 
   of this and the next 42 lines.  The final "43 times" 
   repeats everything in front of it that many times.


Discussion of this module
----------------------------------------------------------------------------

This command-module creates a powerful voice command for 
editing and cursor movement.  This command's structure can 
be represented by the following simplified language model:

 - *CommandRule* -- top-level rule which the user can say
    - *repetition* -- sequence of actions (name = "sequence")
       - *KeystrokeRule* -- rule that maps a single 
         spoken-form to an action
    - *optional* -- optional specification of repeat count
       - *integer* -- repeat count (name = "n")
       - *literal* -- "times"

The top-level command rule has a callback method which is 
called when this voice command is recognized.  The logic 
within this callback is very simple:

1. Retrieve the sequence of actions from the element with 
   the name "sequence".
2. Retrieve the repeat count from the element with the name
   "n".
3. Execute the actions the specified number of times.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

from dragonfly import *
from lib import format

#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up")


#---------------------------------------------------------------------------
# Set up this module's configuration.

config            = Config("multi edit")
config.cmd        = Section("Language section")
config.cmd.map    = Item(
    # Here we define the *default* command map.  If you would like to
    #  modify it to your personal taste, please *do not* make changes
    #  here.  Instead change the *config file* called "_multiedit.txt".
    {
     
    'up [<n>]':    Key('up:%(n)d'),
    'down [<n>]':  Key('down:%(n)d'),
    'lee [<n>]':  Key('left:%(n)d'),
    'rye [<n>]': Key('right:%(n)d'),

    'gope [<n>]':  Key('pgup:%(n)d'),
    'Pad [<n>]':  Key('pgdown:%(n)d'),

    'low [<n>]':  Key('c-left:%(n)d'),
    'row [<n>]':  Key('c-right:%(n)d'),

    'slow [<n>]':  Key('shift:down, c-left:%(n)d, shift:up'),
    'srow [<n>]':  Key('shift:down, c-right:%(n)d, shift:up'),

    'home':        Key('home'),
    'feen':        Key('end'),

    'file top':    Key('c-home'),
    'file toe':    Key('c-end'),

    #### Various keys
    'ace [<n>]':         Key('space:%(n)d'),
    'act':               Key('escape'),
    'chuck [<n>]':       Key('del:%(n)d'),
    'scratch [<n>]':     Key('backspace:%(n)d'),
    'slap [<n>]':        Key('enter:%(n)d'),
    'tab [<n>]':         Key('tab:%(n)d'),
    'untab [<n>]':         Key('shift:down, tab:%(n)d, shift:up'),
' copy':         Key('c-c'),

    #### Lines
    'line down [<n>]': Key('home:2, shift:down, end:2, shift:up, c-x, del, down:%(n)d, home:2, enter, up, c-v'),
    'lineup [<n>]':    Key('home:2, shift:down, end:2, shift:up, c-x, del, up:%(n)d, home:2, enter, up, c-v'),
    'nab [<n>]':       Key('home:2, shift:down, down:%(n)d, up, end:2, shift:up, c-c, end:2'),
    'plop [<n>]':      Key('c-v:%(n)d'),
    'see up [<n>]':      Key('shift:down, up:%(n)d, shift:up'),
    'see down [<n>]':      Key('shift:down, down:%(n)d, shift:up'),
	'see home ':      Key('shift:down, home, shift:up'),
	'see feen':      Key('shift:down, end, shift:up'),
	'comment':      Key('c-slash'),
    
	### Words
    'bump [<n>]':      Key('c-del:%(n)d'),
    'whack [<n>]':     Key('c-backspace:%(n)d'),

	"(Alpha)": Key("a"),
    "(bravo) ": Key("b"),
    "(Coke) ": Key("c"),
    "(delta) ": Key("d"),
    "(echo) ": Key("e"),
    "(fox) ": Key("f"),
    "(golf) ": Key("g"),
    "(hotel) ": Key("h"),
    "(item) ": Key("i"),
    "(John) ": Key("j"),
    "(king) ": Key("k"),
    "(love) ": Key("l"),
    "(mike) ": Key("m"),
    "(nuts) ": Key("n"),
    "(orc) ": Key("o"),
    "(prep) ": Key("p"),
    "(quiche) ": Key("q"),
    "(Roger) ": Key("r"),
    "(sugar) ": Key("s"),
    "(tango) ": Key("t"),
    "(uncle) ": Key("u"),
    "(victor) ": Key("v"),
    "(whiskey) ": Key("w"),
    "(x-ray) ": Key("x"),
    "(yak) ": Key("y"),
    "(zulu) ": Key("z"),

     'capAlpha': Key('A'),
    'capbravo': Key('B'),
    'capCoke': Key('C'),
    'capdelta': Key('D'),
    'capecho': Key('E'),
    'capfox': Key('F'),
    'capgolf': Key('G'),
    'caphotel': Key('H'),
    'capking': Key('K'),
    'capmike': Key('M'),
    'caporc': Key('O'),
    'capprep': Key('P'),
    'capquiche': Key('Q'),
    'captango': Key('T'),
    'capvictor': Key('V'),
    'capwhiskey': Key('W'),
    'capxray': Key('X'),
    'capyak': Key('Y'),
    'capzulu': Key('Z'),
    
    "capuncle": Key("U"    )
    , "capnuts": Key("N"   )
    , "capitem": Key("I"   )
    , "capjohn": Key("J" )
    , "caplove": Key("L"   )
    , "capsugar": Key("S"  )
    , "caproger": Key("R"  ),
    
"eek ": Key("equal"),
"rail": Key("underscore"),
"dot ": Key("dot"),
"whoops ": Key("c-z"),
"save it": Key("c-s"),
"quote": Key("squote"),
    "amp": Key("ampersand"),
    "ash": Key("slash"),
    "atsign": Key("at"),
    "backash": Key("backslash"),
    "backtick": Key("backtick"),
    "bang": Key("bang"),
    "bar": Key("bar"),
    "dollar": Key("dollar"),
    "dot": Key("dot"),
    "drip": Key("comma"),
    "eek": Key("equal"),
    "hat": Key("caret"),
    "hyph": Key("minus"),
    "percent": Key("percent"),
    "pop": Key("rparen"),
    "pound": Key("hash"),
    "push": Key("lparen"),
    "quest": Key("question"),
    "quote": Key("dquote"),
    "rail": Key("underscore"),
    # "semi": Key("semicolon"),
    "smote": Key("squote"),
    "sol": Key("star"),
    "tilde": Key("tilde"),
    "yeah": Key("colon"),

    "bitore": Key("bar"),
    "bitand": Key("and"),
    "bitexor": Key("caret"),
    "divided": Key("slash"),
    "plus": Key("plus"),
    "minus": Key("minus"),
    'boxso': Key('lbrace'),
    'boxco': Key('rbrace'),
    'squareso': Key('lbracket'),
    'squareco': Key('rbracket'),

"zero": Key("0"),
    "one": Key("1"),
    "two": Key("2"),
    "three": Key("3"),
    "four": Key("4"),
    "five": Key("5"),
    "six": Key("6"),
    "seven": Key("7"),
    "eight": Key("8"),
    "nine": Key("9"),

    "drip": Key("comma"),
    "push": Key("lparen"),
    "pop": Key("rparen"),

	# format text
	"score <text>": Function(format.snake_case_text),
	"say <text>": Text('%(text)s'),
    },
	
    namespace={
     "Key":   Key,
     "Text":  Text,
    }
)

namespace = config.load()

#---------------------------------------------------------------------------
# Here we prepare the list of formatting functions from the config file.

# Retrieve text-formatting functions from this module's config file.
#  Each of these functions must have a name that starts with "format_".
format_functions = {}
if namespace:
    for name, function in namespace.items():
     if name.startswith("format_") and callable(function):
        spoken_form = function.__doc__.strip()

        # We wrap generation of the Function action in a function so
        #  that its *function* variable will be local.  Otherwise it
        #  would change during the next iteration of the namespace loop.
        def wrap_function(function):
            def _function(dictation):
                formatted_text = function(dictation)
                Text(formatted_text).execute()
            return Function(_function)

        action = wrap_function(function)
        format_functions[spoken_form] = action


# Here we define the text formatting rule.
# The contents of this rule were built up from the "format_*"
#  functions in this module's config file.
if format_functions:
    class FormatRule(MappingRule):

        mapping  = format_functions
        extras   = [Dictation("dictation")]

else:
    FormatRule = None


#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these 
#  include special elements like the number with name "n" 
#  or the dictation with name "text".  This rule is not 
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when 
#  processing a recognition will be the right side of the 
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html
class KeystrokeRule(MappingRule):

    exported = False

    mapping  = config.cmd.map
    extras   = [
                IntegerRef("n", 1, 100),
                Dictation("text"),
                Dictation("text2"),
               ]
    defaults = {
                "n": 1,
               }
    # Note: when processing a recognition, the *value* of 
    #  this rule will be an action object from the right side 
    #  of the mapping given above.  This is default behavior 
    #  of the MappingRule class' value() method.  It also 
    #  substitutes any "%(...)." within the action spec
    #  with the appropriate spoken values.


#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

# First we create an element that references the keystroke rule.
#  Note: when processing a recognition, the *value* of this element
#  will be the value of the referenced rule: an action.
alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
if FormatRule:
    alternatives.append(RuleRef(rule=FormatRule()))
single_action = Alternative(alternatives)

# Second we create a repetition of keystroke elements.
#  This element will match anywhere between 1 and 16 repetitions
#  of the keystroke elements.  Note that we give this element
#  the name "sequence" so that it can be used as an extra in
#  the rule definition below.
# Note: when processing a recognition, the *value* of this element
#  will be a sequence of the contained elements: a sequence of
#  actions.
sequence = Repetition(single_action, min=1, max=16, name="sequence")


#---------------------------------------------------------------------------
# Here we define the top-level rule which the user can say.

# This is the rule that actually handles recognitions. 
#  When a recognition occurs, it's _process_recognition() 
#  method will be called.  It receives information about the 
#  recognition in the "extras" argument: the sequence of 
#  actions and the number of times to repeat them.
class RepeatRule(CompoundRule):

    # Here we define this rule's spoken-form and special elements.
    spec     = "<sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
                sequence,                 # Sequence of actions defined above.
                IntegerRef("n", 1, 100),  # Times to repeat the sequence.
               ]
    defaults = {
                "n": 1,                   # Default repeat count.
               }

    # This method gets called when this rule is recognized.
    # Arguments:
    #  - node -- root node of the recognition parse tree.
    #  - extras -- dict of the "extras" special elements:
    #     . extras["sequence"] gives the sequence of actions.
    #     . extras["n"] gives the repeat count.
    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]   # A sequence of actions.
        count = extras["n"]             # An integer repeat count.
        for i in range(count):
            for action in sequence:
                action.execute()
        release.execute()


#---------------------------------------------------------------------------
# Create and load this module's grammar.

grammar = Grammar("multi edit")   # Create this module's grammar.
grammar.add_rule(RepeatRule())    # Add the top-level rule.
grammar.load()                    # Load the grammar.

# Unload function which will be called at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
