from dropbox import Dropbox
from objectHandler import RootSynapseLoader, ArgumentReader
from commandProcessor import CommandProcessor


def main():

    synapse = RootSynapseLoader('.root_synapse')
    reader = ArgumentReader()

    processor = CommandProcessor(synapse=synapse, reader=reader)
    processor.digest()


if __name__ == "__main__":
    main()
