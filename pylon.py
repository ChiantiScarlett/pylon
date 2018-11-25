from colorama import init, Fore, Style
from command import Command
from core import TreeStack


class Pylon:
    def __init__(self, dbx):
        init()  # Initialize colorama
        """ Based on the assumption that dbx class is secured. """
        self.dbx = dbx
        self.username = dbx.users_get_current_account().name.familiar_name
        self.cmd = Command()
        self.tree_stack = TreeStack()

    def mainloop(self):
        while True:
            raw_str = input("{}{}@Pylon{} ~ ${} "
                            .format(Fore.RED + Style.BRIGHT,
                                    self.username,
                                    Fore.BLUE,
                                    Fore.RESET + Style.NORMAL))
            # Take care of semicolon
            raw_cmds = raw_str.split(';')

            for raw_cmd in raw_cmds:
                self.cmd.run(raw_cmd)
