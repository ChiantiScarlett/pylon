###############################################################################
# filename: commandProcessor.py

###############################################################################

import subprocess
from colorama import init, Fore, Back, Style
import argparse
import shlex
import sys


class Commands:
    def __init__(self):
        self.action_table = {
            'cd': self.cmd_cd,
            'clear': self.cmd_clear,
            'exit': self.cmd_exit,
            'ls': self.cmd_ls,
            'mkdir': self.cmd_mkdir,
            'new': self.cmd_new,
            'set': self.cmd_set,
            'tree': self.cmd_tree
        }

    def action_wrapper(self, function, *args):
        function(*args)

    def cmd_cd(self, args):
        pass

    def cmd_clear(self, args):
        pass

    def cmd_exit(self, args):
        sys.exit(0)

    def cmd_ls(self, args):
        pass

    def cmd_mkdir(self, args):
        pass

    def cmd_new(self, args):
        pass

    def cmd_set(self, args):
        pass

    def cmd_tree(self, args):
        pass


class CommandProcessor(Commands):
    """
    This class digests input command according to the arguments / parameters
    """

    def __init__(self, synapse):
        super().__init__()
        self.synapse = synapse
        # argparser settings:
        self.reader = argparse.ArgumentParser()
        self.reader.add_argument('action')
        self.reader.add_argument('arguments', nargs="*")

        self.load_initial_screen()

    # Create object handler:
    # synapse = RootSynapse('.root_synapse')
    # processor = CommandProcessor(arguments=args, synapse=synapse)

    def load_initial_screen(self):
        """
        This method loads initial screen
        """
        # Clear screen based on the OS.
        subprocess.call('clear')

    def read_input(self):
        """
        Read input and analyze the command and execute appropriate action.
        """
        command = vars(self.reader.parse_args(shlex.split(input())))
        if command['action'] in self.action_table.keys():
            self.action_wrapper(
                self.action_table[command['action']], command['arguments'])

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

    def show_cursor(self):
        # Show input cursor:
        self.print('➜  ', color='green', style='bright')
        self.print(self.synapse.current_node, color='cyan', style='bright')
        self.print(' ✗ ', color='yellow', style='bright')
