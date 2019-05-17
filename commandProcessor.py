###############################################################################
# filename: commandProcessor.py

###############################################################################

import subprocess
from colorama import init, Fore, Back, Style


class Commands:
    def __init__(self):
        self.synapse = synapse

    def cmd_ls(self, argument):
        pass

    def cmd_cd(self, argument):
        pass

    def cmd_clear(self, argument):
        pass

    def cmd_set(self, argument):
        pass

    def cmd_mkdir(self, argument):
        pass

    def cmd_new(self, argument):
        pass

    def cmd_tree(self, argument):
        pass


class CommandProcessor(Commands):
    """
    This class digests input command according to the arguments / parameters
    """

    def __init__(self, arguments, synapse):
        self.synapse = synapse
        self.flush()

    def load_initial_screen(self):
        """
        This method loads initial screen
        """
        pass

    def print(self, message, fg=None, bg=None, style=None):
        # Foreground color settings:

        fg_map = {'black': Fore.BLACK, 'red': Fore.RED,
                  'green': Fore.GREEN, 'yellow': Fore.YELLOW,
                  'blue': Fore.BLUE, 'magenta': Fore.MAGENTA,
                  'cyan': Fore.CYAN, 'white': Fore.WHITE
                  }

        bg_map = {'black': Back.BLACK, 'red': Back.RED,
                  'green': Back.GREEN, 'yellow': Back.YELLOW,
                  'blue': Back.BLUE, 'magenta': Back.MAGENTA,
                  'cyan': Back.CYAN, 'white': Back.WHITE
                  }

        style_map = {'dim': Style.DIM, 'normal': Style.NORMAL,
                     'bright': Style.BRIGHT}

        if fg in fg_map.keys():
            print(fg_map[fg], end="")
        if bg in bg_map.keys():
            print(bg_map[bg], end="")
        if style in style_map.keys():
            print(style_map[style], end="")

        print(str(message), end="")
        print(Style.RESET_ALL, end="")

    def flush(self):
        # Clear screen based on the OS.
        subprocess.call('clear')

        current_dirs = "/".join(self.synapse.get_parents())
