"""A command module for Dragonfly, for generic editing help.

-----------------------------------------------------------------------------
This is a heavily modified version of the _multiedit-en.py script at:
http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html  # @IgnorePep8
Licensed under the LGPL, see http://www.gnu.org/licenses/

"""

from dragonfly import *  # @UnusedWildImport


class SeriesMappingRule(CompoundRule):

    def __init__(self, mapping, extras=None, defaults=None):
        mapping_rule = MappingRule(mapping=mapping, extras=extras,
            defaults=defaults, exported=False)
        single = RuleRef(rule=mapping_rule)
        series = Repetition(single, min=1, max=16, name="series")

        compound_spec = "<series>"
        compound_extras = [series]
        CompoundRule.__init__(self, spec=compound_spec,
            extras=compound_extras, exported=True)

    def _process_recognition(self, node, extras):  # @UnusedVariable
        series = extras["series"]
        for action in series:
            action.execute()

series_rule = SeriesMappingRule(
    mapping={
        "run it": Key("a-enter"),
		"run down": Key("c-enter"),
		"run chunk": Key("ca-c"),
		"save it": Key("c-s/3"),
		"window one": Key("c-1"),
		"window two": Key("c-2"),
		"dollar": Key("dollar"),
		"comment": Key(" shift:down,c-c,shift:up"),
		"go to function": Key("c-dot"),
		"menu": Key("alt:down,alt:up"),
		"knit it ": Key("shift:down,c-k,shift:up"),
		"run function ": Key("alt:down,c-f,alt:up"),
		"fold it ": Key("a-l"),
		"unfold it ": Key("shift:down,a-l,shift:up"),
		"go to line": Key("shift:down,a-g/3,shift:up"),
		"go to line <n>": Key("shift:down,a-g/3,shift:up") + Text("%(n)d") + Key("enter"),
		"frame right": Key("c-f12"),
		"frame left": Key("c-f11"),
		"nav forward": Key("c-f10"),
		"nav back": Key("c-f9"),
		"nav forward": Key("c-f10"),
		"reformat": Key("shift:down,a-a,shift:up"),
		"lope": Key("c-p"),
		"slope": Key("shift:down,alt:down,c-e,alt:up,shift:up"),
		"find": Key("c-f"),
		"find <text>": Key("c-f") + Text('%(text)s'),
        "find next": Key("f3"),
		"pipe": Key("shift:down,c-m,shift:up"),
		
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)


context = AppContext(executable="rstudio")
terminator_grammar = Grammar("rstudio_control", context=context)
terminator_grammar.add_rule(series_rule)
terminator_grammar.load()


def unload():
    """Unload function which will be called at unload time."""
    global terminator_grammar
    if terminator_grammar:
        terminator_grammar.unload()
    terminator_grammar = None
