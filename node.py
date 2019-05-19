class Node:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.children = {}
        self.name = name

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child_name, isDir=True):
        # print(self.name, "->", child_name)
        if child_name in self.children.keys() and isDir:
            return self.children[child_name]
        else:
            child = Node(name=child_name, parent=self)
            if not isDir:
                child.children = None
            self.children[child_name] = child
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
