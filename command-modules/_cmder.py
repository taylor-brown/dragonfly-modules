#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

"""
Command-module for **Cmdr**
============================================================================


Installation
----------------------------------------------------------------------------

If you are using DNS and Natlink, simply place this file in you Natlink 
macros directory.  It will then be automatically loaded by Natlink when 
you next toggle your microphone or restart Natlink.

Customization
----------------------------------------------------------------------------

Users should customize this module by editing its 
configuration file.  In this file they should edit the 
``search.searchbar`` and ``search.keywords`` settings to 
match their own personal search preferences.  These 
variables map *what you say* to which *search engines* to 
use.

"""

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r76")
except ImportError:
    pass

from dragonfly import *


#---------------------------------------------------------------------------
# Set up this module's configuration.

config                 = Config("commander control")

config.lang                        = Section("Language section")
config.lang.new_tab                = Item("new (tab | sub)")
config.lang.close_tab              = Item("close (tab | sub)")
config.lang.next_tab               = Item("next tab [<n>]")
config.lang.prev_tab               = Item("(previous | preev) tab [<n>]")

#config.generate_config_file()
config.load()



#---------------------------------------------------------------------------
# Create the main command rule.

class CommandRule(MappingRule):

    mapping = {
        config.lang.new_tab:            Key("c-t"),
        config.lang.close_tab:          Key("c-w"),
        config.lang.next_tab:           Key("c-tab:%(n)d"),
        config.lang.prev_tab:           Key("cs-tab:%(n)d"),

        }
    extras = [
        IntegerRef("n", 1, 20),
        Dictation("text"),
        ]
    defaults = {
        "n": 1,
        }




#---------------------------------------------------------------------------
# Create and load this module's grammar.

context = AppContext(executable="cmder")
grammar = Grammar("commander_general", context=context)
grammar.add_rule(CommandRule())
grammar.load()

print 'loading commander'

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
