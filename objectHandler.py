##############################################################################
# Filename: objectHandler.py
# Description: handle Synapse object.
##############################################################################

import json
import sys


class Node:
    def __init__(self, name):
        self.parent = None
        self.children = {}
        self.name = name

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child_name, isDir=True):
        # print(self.name, "->", child_name)
        if child_name in self.children.keys() and isDir:
            return self.children[child_name]
        else:
            child = Node(child_name)
            if not isDir:
                child.child = None
            self.children[child_name] = child
            return child

    def __str__(self):
        return '<'+self.name+'>'


class RootSynapse:
    """
    <local file handler>
    """

    def __init__(self, path):
        """
        Class object that fabricates data based on the .root_synapse file.
        """

        self.data = None

        try:
            with open(path, 'r') as fp:
                self.data = json.loads(fp.read())['data']
        except FileNotFoundError:
            print('[*] File not found.')
            sys.exit(0)

        self.digest()

    def digest(self):
        """
        Draw tree
        """
        self.tree = {}

        root_tree = Node(name='Synapse')
        for key in self.data.keys():
            path = self.data[key]['path']
            child = root_tree

            for filename in self.data[key]['path']:
                child = child.add_child(filename)

            child.add_child(self.data[key]['filename'], isDir=False)

    def draw(self, depth=None, head=None):
        """
        Description:
            Print out tree structure on console, similar to the `tree`
            linux command.
        Arguments:
            depth: file depth
            head: number of lines to print
        """

    def get_tags(self):
        """
        Print all the tags.
        """
        pass

    def search_by_tag(self, tag):
        """
        Search Synapse objects that have specific tag
        """
        pass
