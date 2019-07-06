##############################################################################
# Filename: objectHandler.py
# Description: handle Synapse object.
##############################################################################

import json
import sys
import argparse
from core import Console


class _Node:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.isDir = True
        self.name = name
        self.children = {}
        self.filsize = None

    def add_child(self, name):
        if name in self.children.keys():
            return self.children[name]
        else:
            child = _Node(name=name, parent=self)
            self.children[name] = child
            return child

    def print(self, depth=[], isLastItem=False, isLastRow=True):
        """
        Recursive printing method => display a tree structure on the console.
        """

        if depth == []:
            print('.')

        for item in depth:
            print(item, end="")

        if isLastRow and not self.children:
            print('└──', self.name)
        else:
            print('├──', self.name)

        if not self.children:
            return
        else:
            if len(self.children) > 1:
                for child in list(self.children.keys())[:-1]:
                    self.children[child].print(
                        depth=depth+['│   '], isLastRow=False)

            self.children[list(self.children.keys())[-1]
                          ].print(depth=depth+["│   "], isLastRow=True)

    def __str__(self):
        return self.name


class SynapseLoader:
    """
    This class loads `.synapse` file and draw virtual directory structure using
    `_Node` class.
    """

    def __init__(self, path):
        self.console = Console()
        try:
            with open(path, 'r') as fp:
                data = json.loads(fp.read())
        except json.JSONDecodeError:
            self.console.raise_error(
                'Invalid format in `.synapse` file.', type="CRITICAL")

        self.key = list(data.keys())[0]
        self.name = data[self.key]['object_name']
        self.components = data[self.key]['components']
        self.structure = None

        self.digest()

    def digest(self):
        """
        create a structure with virtualized structure with _Node() file
        """
        # Create object directory structure:
        path_list = self.name.split('/')
        self.structure = _Node(name=path_list[0], parent=None)
        cursor = self.structure
        path_list.pop(0)
        for path in path_list:
            cursor = cursor.add_child(path)

        # Add components into the structure
        obj_cursor = cursor
        for key in self.components.keys():
            cursor = obj_cursor
            filename = self.components[key]['filename']
            for file in filename.split('/'):
                cursor = cursor.add_child(file)

            cursor.isDir = False  # Last cursor should be a file object
            cursor.filesize = self.components[key]['filesize']


class RootSynapseLoader(SynapseLoader):
    def __init__(self):
        super().__init__()
