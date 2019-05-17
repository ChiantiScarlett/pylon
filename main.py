from dropbox import Dropbox
from objectHandler import RootSynapse
from commandProcessor import CommandProcessor


def main():

    synapse = RootSynapse('.root_synapse')
    processor = CommandProcessor(synapse=synapse)

    while True:
        processor.show_cursor()
        processor.read_input()


if __name__ == "__main__":
    main()
