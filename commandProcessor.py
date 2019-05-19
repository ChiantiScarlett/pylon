###############################################################################
# filename: commandProcessor.py

###############################################################################

from os import popen
from colorama import init, Fore, Back, Style
import sys


class Commands:
    def __init__(self):
        self.action_table = {
            'tree': self.cmd_tree
        }

    def action_wrapper(self, function, *args):
        function(*args)

    def cmd_tree(self, args):
        self.synapse.root_node.print()


class CommandProcessor(Commands):
    """
    This class digests input command according to the arguments / parameters
    """

    def __init__(self, synapse, reader):
        super().__init__()
        self.synapse = synapse
        self.reader = reader

    def digest(self):
        """
        Read input, analyze the command and execute appropriate action.
        """
        command = self.reader.digest()
        print(command)
        if command['action'] in self.action_table.keys():
            self.action_wrapper(
                self.action_table[command['action']], command['arguments'])
        else:
            self.print("[*] No argument specified.")

    def print(self, message, color=None, background=None, style=None):
        """
        Print a string with specific color, background, style settings.
        """
        # Foreground color settings:

        color_map = {'black': Fore.BLACK, 'red': Fore.RED,
                     'green': Fore.GREEN, 'yellow': Fore.YELLOW,
                     'blue': Fore.BLUE, 'magenta': Fore.MAGENTA,
                     'cyan': Fore.CYAN, 'white': Fore.WHITE
                     }

        background_map = {'black': Back.BLACK, 'red': Back.RED,
                          'green': Back.GREEN, 'yellow': Back.YELLOW,
                          'blue': Back.BLUE, 'magenta': Back.MAGENTA,
                          'cyan': Back.CYAN, 'white': Back.WHITE
                          }

        style_map = {'dim': Style.DIM, 'normal': Style.NORMAL,
                     'bright': Style.BRIGHT}

        if color in color_map.keys():
            print(color_map[color], end="")
        if background in background_map.keys():
            print(background_map[background], end="")
        if style in style_map.keys():
            print(style_map[style], end="")

        print(str(message), end="")
        print(Style.RESET_ALL, end="")

    def raise_error(self, message):
        self.print(message+'\n')
