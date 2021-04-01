from beets.plugins import BeetsPlugin
from beets.ui import Subcommand


my_command = Subcommand('acme', help='demonstrates a plugin')
def hello(lib, opts, args):
    print("This is the Acme plugin.")
my_command.func = hello

class Acme(BeetsPlugin):
    def commands(self):
        return [my_command] 

class Foo():
    pass

