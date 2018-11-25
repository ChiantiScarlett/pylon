class TreeStack:
    def __init__(self):
        self.path = []

    def push(self, new_path):
        self.path.append(new_path)

    def pop(self):
        self.path.pop(-1) if len(self.path) else None

    def print_path(self):
        return "/".join(self.path) if len(self.path) else '/'
