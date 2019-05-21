from commandProcessor import CommandProcessor
from serverHandler import DropboxHandler


def main():
    # handler = DropboxHandler('./settings.json')
    # synapse = RootSynapseLoader('.root_synapse')
    server_handler = DropboxHandler('./settings.json')

    processor = CommandProcessor()
    # processor.set_handler(server_handler)
    processor.digest()


if __name__ == "__main__":
    main()
