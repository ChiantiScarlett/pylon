from colorama import init, Fore, Back, Style
import argparse
import sys


class ArgumentReader:
    """
    This class reads argument from sys.argv, and converts it into
    usable format.
    """

    def __init__(self):
        self.reader = argparse.ArgumentParser()
        self.reader.add_argument('action')
        self.reader.add_argument('arguments', nargs="*")
        self.reader.parse_args()

    def digest(self):
        command = vars(self.reader.parse_args())
        return command


class Console:
    """
    This class deals with console activity, especially for printing out
    specific message with styles. 
    """

    def __init__(self):
        self.ERROR_TYPES = {
            'ERROR': {'color': 'red', 'background': None, 'style': 'bright'},
            'DEFAULT': {'color': None, 'background': None, 'style': None}
        }

    def print(self, message, color=None, background=None, style=None):
        """
        Print a string with specific color, background, style settings.
        """

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

    def raise_error(self, message, type='DEFAULT'):
        if type.upper() not in self.ERROR_TYPES.keys():
            self.raise_error(message='Invalid message type: {}'.format(type))

        self.print('[*] {}\n'.format(message),
                   color=self.ERROR_TYPES[type]['color'],
                   background=self.ERROR_TYPES[type]['background'],
                   style=self.ERROR_TYPES[type]['style'])

        sys.exit(0)
