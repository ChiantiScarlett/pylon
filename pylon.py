from colorama import init, Fore, Back, Style


class Pylon:
    def __init__(self, dbx):
        init()  # Initialize colorama
        """ Based on the assumption that dbx class is secured. """
        self.dbx = dbx
        self.username = dbx.users_get_current_account().name.familiar_name

    def mainloop(self):
        input_cmd = input("{}{}@Pylon{} ~ ${} "
                          .format(Fore.RED + Style.BRIGHT,
                                  self.username,
                                  Fore.BLUE,
                                  Fore.RESET + Style.NORMAL))
