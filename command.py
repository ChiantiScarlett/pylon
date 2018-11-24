import subprocess


class Command:
    def __init__(self):
        self.table = {
            'clear': self.c_clear,
            'cls': self.c_clear
        }

    def run(self, command):
        if command not in self.table.keys():
            print('{}: command not found'.format(command))
        else:
            self.table[command]()

    def c_clear(self):
        subprocess.call('clear')
