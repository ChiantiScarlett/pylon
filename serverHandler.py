import dropbox
from dropbox.stone_validators import ValidationError
import json
from core import Console
from objectHandler import RootSynapseLoader
from os.path import exists

from dropbox.files import WriteMode


class ServerHandler:
    console = None
    settings = None
    rsynapse = None
    API = None

    def __init__(self, settings_path):
        self.console = Console()

        with open(settings_path, 'r') as fp:
            self.settings = json.loads(fp.read())

        self.load_synapse()

    def load_synapse(self):
        """
        Read locally stored `.root_synapse`. If not exists, fetch from the
        server using self.update_rsynapse()
        """
        if not exists(self.settings['LOCAL_STORAGE_PATH']):
            self.update_rsynapse()
        else:
            self.rsynapse = RootSynapseLoader(
                self.settings['LOCAL_STORAGE_PATH'])

    def connect(self):
        """
        Create server API accessible object.
        [ Should be overrided when inherited ]
        """
        self.console.raise_error(
            '`self.connect` was not overrided.', type='CRITICAL')

    def update_rsynapse(self):
        """
        [ Should be overrided when inherited ]
        """
        self.console.raise_error(
            '`self.update_rsynapse` was not overrided.', type='CRITICAL')

    def download_single_file(self, local_path, server_path):
        """
        [ Should be overrided when inherited ]
        """
        self.console.raise_error(
            '`self.download_single_file` was not overrided.', type='CRITICAL')

    def upload_single_file(self, local_path, server_path):
        """
        [ Should be overrided when inherited ]
        """
        self.console.raise_error(
            '`self.upload_single_file` was not overrided.', type='CRITICAL')


class DropboxHandler(ServerHandler):
    """
    <server file handler using Dropbox>
    """

    def __init__(self, settings_path):
        super().__init__(settings_path)

    def download_single_file(self, local_path, server_path):
        """
        [ Overriding from child-side ]
        """
        self.connect() if not self.API else None

        self.API.files_download_to_file(local_path, server_path)

    def upload_single_file(self, local_path, server_path):
        """
        [ Overriding from child-side ]
        """
        self.connect() if not self.API else None

        with open(local_path, 'rb') as fp:
            self.API.files_upload(
                fp.read(), server_path, mode=WriteMode('overwrite'))

    def connect(self):
        """
        [ Overriding from child-side ]
        """
        self.API = dropbox.Dropbox(self.settings['DROPBOX_ACCESS_TOKEN'])

    def update_rsynapse(self):
        """
        [ Overriding from child-side ]
        """
        self.connect() if not self.API else None
        try:
            f = self.API.files_list_folder(
                '/'+self.settings['DROPBOX_ROOT_PATH'].strip('/')).entries
        except ValidationError:
            self.console.raise_error(
                message='No such directory found on the server: `{}`'.format(
                    '/'+self.settings['DROPBOX_ROOT_PATH'].strip('/')),
                type='ERROR')
