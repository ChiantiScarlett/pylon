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
            print(block, 'idx: ', loop_idx)


            if block in digested_cmd['flag'].keys():
                digested_cmd['flag'][block] = True
                loop_idx += 1
            # elif block in digested_cmd['sval'].keys():
            #     while loop_idx < len(cmd):
            #         try:
            #             loop_idx += 1
            #             if cmd[loop_idx].startswith('-'):
            #                 raise Exception
            #             digested_cmd['sval'][block] = cmd[loop_idx]

            #             # Check if the input has single value
            #             if loop_idx + 1 < len(cmd):
            #                 if not cmd[loop_idx + 1].startswith('-'):
            #                     raise Exception

            #         except Exception:
            #             # Exception for IndexError as well
            #             print("{}: invalid option -- {}".format(cmd[0], block.strip('-')))
            #             return None


            # elif block in digested_cmd['sval'].keys():
            #     try:
            #         loop_idx += 1
            #         if cmd[loop_idx].startswith('-'):
            #             raise Exception
            #         digested_cmd['sval'][block] = cmd[loop_idx]
            #     except:
            #         # Exception for IndexError as well
            #         print("{}: invalid option -- {}".format(cmd[0], block.strip('-')))
            #         return None

            # elif block.startswith('-'):
            #     print("{}: invalid option -- {}".format(cmd[0], block.strip('-')))
            #     return None

            else:
                digested_cmd['args'].append(block)
                loop_idx += 1


        return digested_cmd



    def c_clear(self, raw_cmd):
        subprocess.call('clear')

    def c_cd(self, raw_cmd):
        opts = self.digest(raw_cmd,
                           flag=['-f'],
                           sval=['-s'],
                           mval=['-m'],
                           args=[],
                           singleArg=False
                           )
        print(opts)

    def c_exit(self, raw_cmd):
        sys.exit()
