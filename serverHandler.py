import dropbox
from dropbox.stone_validators import ValidationError
import json
from core import Console


class DropboxHandler:
    """
    <server file handler>
    """

    def __init__(self, settings_path):
        """
        Create a dropbox object via Dropbox API, and get the file.
        """

        self.console = Console()

        with open(settings_path, 'r') as fp:
            data = json.loads(fp.read())
            self._access_token = data['access_token']
            self._root_path = data['root_path']

        self.connect()

    def connect(self):
        """
        Connect Dropbox object with keys from settings.json and initialize
        the class.
        """
        dbx = dropbox.Dropbox(self._access_token)
        try:
            f = dbx.files_list_folder('/'+self._root_path.strip('/')).entries
        except ValidationError:
            self.console.raise_error(
                message='dropbox: No directory found: `{}`'.format(
                    '/'+self._root_path.strip('/')),
                type='ERROR')

    def read_root_synapse(self):
        """
        Read .root_synapse file from the Dropbox server.
        """

    def create(self, path):
        """
        Create a new synapse object.
        """
        pass

    def upload(self, path):
        """
        Upload an object to the Dropbox.
        """
        pass

    def update(self, path):
        """
        Update .root_synapse based on the file change.
        """
        pass
