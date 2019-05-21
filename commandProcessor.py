###############################################################################
# filename: commandProcessor.py

###############################################################################

from os import popen
from os.path import exists
import sys
from core import Console, ArgumentReader
from serverHandler import DropboxHandler
from objectHandler import RootSynapseLoader, SynapseLoader


class _Commands:
    def __init__(self):
        self.action_table = {
            'tree': self.cmd_tree,
            'mkdir': self.cmd_mkdir,
            'rmdir': self.cmd_rmdir,
            'touch': self.cmd_touch,
            'rm': self.cmd_rm,
            'mv': self.cmd_mv,
            'tmp': self.cmd_tmp
        }

    def action_wrapper(self, function, *args):
        function(*args)

    def cmd_tree(self, args):
        self.synapse.root_node.print()

    def cmd_mkdir(self, args):
        pass

    def cmd_rmdir(self, args):
        pass

    def cmd_touch(self, args):
        pass

    def cmd_rm(self, args):
        pass

    def cmd_mv(self, args):
        pass

    def cmd_tmp(self, args):
        pass  # Test


class CommandProcessor(_Commands):
    """
    1. Read input using ArgumentParser
    2. Run appropriate command
    """

    def __init__(self):
        # Initialize command-related methods:
        super().__init__()

        self.synapse = None
        self.console = Console()
        self.handler = None

    def set_handler(self, handler):
        self.handler = handler

    def digest(self):
        """
        """
        # Check if the handler is defined, else raise Error:
        if type(self.handler) not in [DropboxHandler]:
            self.console.raise_error(
                'Invalid or undefined server handler.', type='ERROR')

        # Initialize argument parser and read arguments:
        command = ArgumentReader().digest()

        # Read synapse file from current directory:
        if exists('.synapse'):
            self.synapse = SynapseLoader(".synapse")
        elif exists('.root_synapse'):
            self.synapse = RootSynapseLoader(".root_synapse")
        else:
            self.console.raise_error(
                'No `.synapse` file found. Make sure you are under '
                'Synapse object directory.', type='ERROR')

        # Run following command:
        if command['action'] in self.action_table.keys():
            self.action_wrapper(
                self.action_table[command['action']], command['arguments'])
        else:
            self.console.print("[*] No argument specified.")
