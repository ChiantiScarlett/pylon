import subprocess
import sys
import shlex


class Command:
    def __init__(self):
        self.table = {
            'cd': self.c_cd,
            'clear': self.c_clear,
            'cls': self.c_clear,
            'exit': self.c_exit,
        }

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
               args=[],
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
                print("{}: invalid option -- {}".format(cmd[0], block.strip('-')))
                return None

            # Other wise consider it as `argument`
            else:
                digested_cmd['args'].append(block)
                loop_idx += 1

        return digested_cmd

    def c_clear(self, raw_cmd):
        subprocess.call('clear')

    def c_cd(self, raw_cmd):
        opts = self.digest(raw_cmd,
                           flag=['-q'],
                           sval=['-s'],
                           mval=['-m'],
                           args=[],
                           singleArg=False
                           )
        from pprint import pprint
        pprint(opts)

    def c_exit(self, raw_cmd):
        sys.exit()
