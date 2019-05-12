import subprocess
import sys
import shlex


class Command:
    def __init__(self, dbx, tree_stack):
        self.table = {
            'cd': self.c_cd,
            'clear': self.c_clear,
            'cls': self.c_clear,
            'exit': self.c_exit,
        }
        self.dbx = dbx
        self.tree_stack = tree_stack

    def run(self, raw_cmd):
        # Do nothing if input_cmd is ''
        if raw_cmd.strip() == '':
            return

        # Find command
        cmd = raw_cmd if raw_cmd.find(' ') == -1 else raw_cmd.split()[0]

        # If command not found, toast an error message
        if cmd not in self.table.keys():
            print('{}: command not found'.format(cmd))
        # Else run the command
        else:
            self.table[cmd](raw_cmd)

    def digest(self, raw_cmd,
               flag=[],
               sval=[],
               mval=[],
               singleArg=False):
        """
        Read and analyze options

        Return 0 to halt
        Otherwise return digested_cmd
        """

        # Set framework:
        digested_cmd = {
            'flag': {},
            'sval': {},
            'mval': {},
            'args': [],
            'singleArg': singleArg
        }

        # flag :: set default value to False
        for item in flag:
            digested_cmd['flag'][item] = False
        # sval :: set default value to None
        for item in sval:
            digested_cmd['sval'][item] = None
        # mval :: set default value to list()
        for item in mval:
            digested_cmd['mval'][item] = []

        cmd = shlex.split(raw_cmd)

        loop_idx = 1
        while loop_idx < len(cmd):
            block = cmd[loop_idx]

            # Check if flag is set
            if block in digested_cmd['flag'].keys():
                digested_cmd['flag'][block] = True
                loop_idx += 1

            # Check if single-value key is set
            elif block in digested_cmd['sval'].keys():
                try:
                    loop_idx += 1
                    if cmd[loop_idx].startswith('-'):
                        raise Exception
                    digested_cmd['sval'][block] = cmd[loop_idx]
                    loop_idx += 1

                except Exception:
                    # Exception for IndexError as well
                    print(
                        "{}: invalid option -- {}".format(cmd[0], block.strip('-')))
                    return None

            # Check if multi-value keys are set
            elif block in digested_cmd['mval'].keys():
                try:
                    loop_idx += 1
                    if cmd[loop_idx].startswith('-'):
                        raise Exception
                    digested_cmd['mval'][block] = [cmd[loop_idx]]
                    loop_idx += 1

                except Exception:
                    # Exception for IndexError as well
                    print(
                        "{}: invalid option -- {}".format(cmd[0], block.strip('-')))
                    return None

                # Read more value until it meets the end or other option
                while loop_idx < len(cmd):
                    if not cmd[loop_idx].startswith('-'):
                        digested_cmd['mval'][block].append(cmd[loop_idx])

                        loop_idx += 1
                    else:
                        break

            # Filter out unidentified options
            elif block.startswith('-'):
                print("{}: invalid option -- {}".format(cmd[0],
                    block.strip('-')))
                return None

            # Other wise consider it as `argument`
            else:
                digested_cmd['args'].append(block)

                # If singleArg is True, raise Error
                if singleArg and len(digested_cmd['args']) > 1:
                    print(
                        "{}: invalid option -- too many arguments".format(cmd[0]))

                loop_idx += 1

        return digested_cmd

    def c_clear(self, raw_cmd):
        subprocess.call('clear')

    def c_cd(self, raw_cmd):
        opts=self.digest(raw_cmd,
                           flag=[],
                           sval=[],
                           mval=[],
                           singleArg=True
                           )

        # Empty path: Do nothing
        if len(opts['args']) == 0:
            return

        # Strip rightside '/'
        path = opts['args'][0]
        path = path[:-1] if path.endswith('/') else path

        # Split path
        routes = path.split('/')

        for path in routes:
            if path == '..':
                self.tree_stack.pop()
            else:
                status_OK = self.tree_stack.push(path)
                if not status_OK:
                    print("cd: {}: No such file or directory"
                        .format(path))
                return





    def c_exit(self, raw_cmd):
        sys.exit()
