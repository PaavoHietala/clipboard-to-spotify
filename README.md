# clipboard-to-spotify
Create a spotify playlist based on your clipboard contents. Expected input format is a copied table from a website, which is transformed to a cell-per-line string on your clipboard.

## Installation

1. Install required packages using
    ```
    python -m pip install -r requirements.txt
    ```
2. Login to [Spotify developer dashboard](https://developer.spotify.com/dashboard) and create a new app. You can give any name and description for the app, but the redirect URI has to be exactly the same as in the `config.ini` file below. By default you should use http://localhost:8888/callback/. Save the app info and go to your new app's settings. Check your Client ID and Client secret, which are used in the next step.
3. Create a `config.ini` and verify the settings. A template of the file is automatically created if missing, but you need to input your Spotify API keys there. You can leave the `redirect_uri` as-is to enable automatic token retrieval.
    ```
    [DEFAULT]
    client_id=<spotify client ID>
    client_secret=<spotify client secret>
    redirect_uri=http://localhost:8888/callback/
    ```

## Usage

1. Select and copy a table's contents from a website or other program of your choice. This script was originally written to create playlists from Finland's top 75 hits published [here](https://suomenvuosilistat.blogspot.com/).
2. Start the script by running the following command:
    ```
    python generate_playlist.py
    ```
3. Input the number of columns in your data as requested by the script.
    ```
    How many columns does your data have?
    3
    ```
4. Check the preview of the formatted table and input a name & an optional description for the playlist.
    ```
    Partial table preview (75 rows in total):

        0                     1                         2 3
    0  1           Rasmus, The            IN THE SHADOWS
    1  2  Don Johnson Big Band         ONE MC, ONE DELAY
    2  3      Williams, Robbie                      FEEL
    3  4                    Yö  RAKKAUS ON LUMIVALKOINEN
    4  5                Eminem             LOSE YOURSELF

    Give a name for the playlist: Suomen Top 75 2003
    Give a description for the playlist (optional): Suomen suurimmat hitit vuodelta 2003.
    ```
5. Input the indices for columns containing the song names and artist names as requested. The indices are shown in the table preview in the previous step.
    ```
    Created playlist Suomen Top 75 2003
    Which column has the song names? (0-3): 2
    Which column has the artist names? (0-3): 1
    ```
6. The script will now build a playlist based on the given data. Check your Spotify account to confirm that the playlist has been successfully created.
    ```
    Found the song The Rasmus                               In the Shadows                           spotify:track:1fr92Vupmcs2vgLMFVQ7rd
    Found the song Don Johnson Big Band                     One MC, One Delay                        spotify:track:6mCxTrPBzi0OR2U7LVxkGB
    ...
    Found the song Gimmel                                   Harmaata lunta                           spotify:track:1zt3OemlFSug4hDShpvxRp
    Found the song Pikku G                                  Romeo ja Julia (feat. Sophie)            spotify:track:0seHreoI3kwp38OlEgLLnT
    Adding items to playlist Suomen Top 75 2003
    Finished buildng the playlist.
    ```

## Todo

- Remove a playlist in case of an error to prevent filling the user's library with empty/failed playlists.
- Compute a similarity score between the search string and the search result to trigger a not-found warning instead of adding a random song to the playlist
