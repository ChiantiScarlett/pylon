from dropbox import Dropbox
from objectHandler import RootSynapse
from commandProcessor import CommandProcessor
import argparse


def main():
    # Parse arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help="action: [new, get, commit, push]")
    parser.add_argument('arguments', nargs="*", help="options")
    args = vars(parser.parse_args())

    # Create object handler:
    handler = RootSynapse('.root_synapse')
    processor = CommandProcessor(arguments=args, handler=handler)


if __name__ == "__main__":
    main()
