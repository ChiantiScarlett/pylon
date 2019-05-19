##############################################################################
# Filename: objectHandler.py
# Description: handle Synapse object.
##############################################################################

import json
import sys
import argparse
from node import Node


class RootSynapseLoader:
    """
    <local file handler>
    """

    def __init__(self, path):
        """
        Class object that fabricates data based on the .root_synapse file.
        """

        self.data = None
        self.root_node = None
        self.parent = None
        self.current_node = None

        try:
            with open(path, 'r') as fp:
                self.data = json.loads(fp.read())['data']
        except FileNotFoundError:
            print('[*] File not found.')
            sys.exit(0)

        self.digest()
        self.current_node = self.root_node

    def digest(self):
        """
        Convert dict object from `self.data` to tree-shape Node class.
        """

        self.root_node = Node(name='Synapse', parent=None)
        for key in self.data.keys():
            path = self.data[key]['path']
            child = self.root_node

            for filename in self.data[key]['path']:
                child = child.add_child(filename)

            child.add_child(self.data[key]['filename'], isDir=False)

    def tree(self, depth=None, head=None):
        """
        Description:
            Print out tree structure on console, similar to the `tree`
            linux command.
        Arguments:
            depth: file depth
            head: number of lines to print
        """
        self.root_node.print()

    def get_parents(self):
        """
        Returns list of parent hierarchy names
        """
        cursor = self.current_node
        parents_list = []
        while cursor != None:
            parents_list.append(cursor.name)
            cursor = cursor.parent
        return parents_list


class ArgumentReader:
    def __init__(self):
        self.reader = argparse.ArgumentParser()
        self.reader.add_argument('action')
        self.reader.add_argument('arguments', nargs="*")
        self.reader.parse_args()

    def digest(self):
        command = vars(self.reader.parse_args())
        return command
