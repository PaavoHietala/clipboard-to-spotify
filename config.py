import os
import configparser

from sys import exit

class _Config:
    '''
    A private class for storing all runtime options from config.ini.
    The class is used via "from config import config" which creates
    a _Config object if it does not exist yet.

    Options are accessed via config.<option>.
    '''

    def __init__(self):
        '''Load config.ini or create one if it doesn't exist.'''

        cfgpath = os.path.join(os.path.dirname(__file__), 'config.ini')

        if os.path.isfile(cfgpath):
            self.config = configparser.ConfigParser()
            self.config.read(cfgpath)
        else:
            with open(cfgpath, 'w') as f:
                f.write('[DEFAULT]\nclient_id=\nclient_secret=\n'
                        + 'redirect_uri=http://localhost:8888/callback/')
            print('Created config.ini. Please add your client ID and secret in'
                  + ' the file and run the script again.')
            exit()

    def __getattr__(self, name):
        '''
        Enable option retrieval using config.<option> instead of using
        config.config.get("DEFAULT", <option>).

        Parameters
        ----------
        name : str
            Option name to retrieve.

        Returns
        -------
        str
            Value of the requested option.
        '''

        try:
            return self.config.get('DEFAULT', name)
        except KeyError:
            print(f"Config does not have the attribute '{name}'")

config = _Config()