###############################################################################
# filename: commandProcessor.py

###############################################################################

from os import popen
from os.path import exists
from os import mkdir
import json
from hashlib import md5
from datetime import datetime
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
            'tmp': self.cmd_tmp,
            'new': self.cmd_new,
            'clone': self.cmd_clone
        }

    def action_wrapper(self, function, *args):
        function(*args)

    def cmd_new(self, args):
        """
        Create new Synapse object
        """
        for arg in args:  # arg is the object name
            mkdir(arg)
            with open(arg+'/.synapse', 'w') as fp:
                # Write default state:
                data = {}
                data[md5(str(datetime.now()).encode('utf-8')).hexdigest()] = {
                    "object_name": arg, "components": {}}

                fp.write(json.dumps(data))

    def cmd_clone(self, args):
        """
        Download Synapse object from server
        """
        # Verify argument
        if len(args) == 0:
            self.console.raise_error(
                'Command `clone` must have at least one argument of '
                'object ID or alias.', type="ERROR")

        # Read .root_synapse file.
        rsynapse = self.handler.read_rsynapse()

        for arg in args:  # arg is the Synapse object ID name
            # Validate object ID or alias
            if arg not in rsynapse['data'].keys():
                self.console.raise_error(
                    'Cannot find Synapse object which has ID or alias: `{}`'.format(
                        arg),
                    type="ERROR")
            # Clone object
            synapse = rsynapse['data'][arg]

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
