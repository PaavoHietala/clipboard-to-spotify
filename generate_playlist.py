import pyperclip
import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config import config

def raw_to_df(raw):
    '''
    Transform raw table data in <raw> to a pandas dataframe format.

    Parameters
    ----------
    raw : str
        Raw data string from clipboard
    
    Returns
    -------
    df : pandas.DataFrame

    '''

    cols = int(input('How many columns does your data have?\n'))
    raw = [line.strip() for line in raw.split('\n') if line.strip()]

    df = pd.DataFrame([raw[i:i + cols] for i in range(0, len(raw), cols)])
    df[df.shape[1]] = ''

    print(f'\nPartial table preview ({df.shape[0]} rows in total):\n\n',
          df.head(), '\n')

    return df

def spotify_auth():
    auth = SpotifyOAuth(client_id = config.client_id,
                        client_secret = config.client_secret,
                        scope = 'playlist-modify-private',
                        redirect_uri = config.redirect_uri)
    sp = spotipy.Spotify(auth_manager = auth)

    return sp

def create_playlist(sp):
    name = input('Give a name for the playlist: ')
    desc = input('Give a description for the playlist (optional): ')
    playlist = sp.user_playlist_create(sp.me()['id'], name, description = desc,
                                       public = False, collaborative = False)

    print(f'Created playlist {name}')

    return playlist

def add_uris_to_df(sp, df):
    song_col = int(input(f'Which column has the song names? (0-{df.shape[1] - 1}): '))
    artist_col = int(input(f'Which column has the artist names? (0-{df.shape[1] - 1}): '))

    for idx, row in df.iterrows():
        result = sp.search(f'{row[artist_col]} {row[song_col]}', limit = 1)
        print(f'Found the song {result["tracks"]["items"][0]["artists"][0]["name"][:40]:40} '
              + f'{result["tracks"]["items"][0]["name"][:40]:40} '
              + f'{result["tracks"]["items"][0]["uri"]}')
        df.iloc[idx, df.shape[1] - 1] = result["tracks"]["items"][0]["uri"]

    return df

def add_songs_to_playlist(sp, df, playlist):
    print(f'Adding items to playlist {playlist["name"]}')
    sp.playlist_add_items(playlist['id'], df[df.shape[1] - 1].tolist())

    return None

if __name__ == '__main__':
    raw = pyperclip.paste()

    if raw == '':
        print('Clipboard is empty. Copy a table to clipboard and restart the script.')
    else:
        df = raw_to_df(raw)
        sp = spotify_auth()
        playlist = create_playlist(sp)
        df = add_uris_to_df(sp, df)
        add_songs_to_playlist(sp, df, playlist)

        print("Finished buildng the playlist.")
