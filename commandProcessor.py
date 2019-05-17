###############################################################################
# filename: commandProcessor.py

###############################################################################

import subprocess


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

    def print(self, message, color=None):
        print(str(message), end="")
        return

    def flush(self):
        # Clear screen based on the OS.
        subprocess.call('clear')

        current_dirs = "/".join(self.synapse.get_parents())
        self.print(current_dirs)
