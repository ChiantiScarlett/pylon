###############################################################################
# filename: commandProcessor.py

###############################################################################

from os import popen
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
        # Check arg length:
        if len(args) == 0:
            self.synapse.current_node = self.synapse.root_node
            return
        elif len(args) != 1:
            self.raise_error('cd: too many arguments.')
            return

        args = args[0]
        # Deal with exceptional situations:
        if args == '..' or args == '/':
            self.synapse.current_node = \
                self.synapse.current_node.parent \
                if self.synapse.current_node.parent \
                else self.synapse.root
            return
        elif args == '.':
            return

        args = args.split('/')
        for arg in args:
            if arg == '..':
                self.synapse.current_node = \
                    self.synapse.current_node.parent if \
                    self.synapse.current_node.parent != None \
                    else self.synapse.current_node
            elif arg in self.synapse.current_node.children.keys():
                self.synapse.current_node = \
                    self.synapse.current_node.children[arg]
            else:
                self.raise_error('cd: no such file or directory: '+arg)
                return

    def cmd_clear(self, args):
        print(popen('clear', 'r').read(), end="")

    def cmd_exit(self, args):
        sys.exit(0)

    def cmd_ls(self, args):
        # Find the longest filename:
        children = list(self.synapse.current_node.children.keys())
        max_length = 0
        for child in children:
            length = len(child) + 2  # extra padding on the right
            # Extra length when unicode character is detected:
            for char in child:
                length += 1 if ord(char) > 128 else 0

            max_length = length if length > max_length else max_length

        # Get current terminal width:
        # **** need to be fixed later for OS compatability ****
        terminal_width = int(popen('stty size', 'r').read().split()[1])

        # Calculate possible column length:
        column_length = int(terminal_width / max_length)
        column_length = 1 if column_length == 0 else column_length

        # Print dir / file names with paddings:
        children.sort()
        for child in children:
            padding_length = int(terminal_width/column_length)
            # Extra removal when unicode character is detected:
            for char in child:
                padding_length -= 2 if ord(char) > 128 else 1

            # Check if the child is directory
            if self.synapse.current_node.children[child].children is not None:
                color = 'cyan'
                style = 'bright'
            else:
                color = None
                style = None
            # Switch rows when the item is on the last column:
            self.print(child+" " * padding_length,
                       color=color, style=style)
            if (children.index(child)+1) % column_length == 0:
                self.print('\n')

        self.print('\n')

    def cmd_mkdir(self, args):
        pass

    def cmd_new(self, args):
        pass

    def cmd_set(self, args):
        pass

    def cmd_tree(self, args):
        self.synapse.root_node.print()


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
        # print(popen('clear', 'r').read(), end="")

    def read_input(self):
        """
        Read input and analyze the command and execute appropriate action.
        """
        command = input()
        if not command:
            return

        command = vars(self.reader.parse_args(shlex.split(command)))
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

    def raise_error(self, message):
        self.print(message+'\n')
