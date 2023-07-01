import pyperclip
import pandas as pd

def raw_to_df(raw):
    '''
    Transform raw table data in <raw> to a pandas dataframe format.

    Parameters
    ----------
    raw : str
        Raw data string from clipboard
    '''

    cols = int(input("How many columns does your data have?\n"))
    raw = [line.strip() for line in raw.split('\n') if line.strip()]

    table = pd.DataFrame([raw[i:i + cols] for i in range(0, len(raw), cols)])

    print("Created a table from clipboard:\n", table.head())

    return table

if __name__ == "__main__":
    raw = pyperclip.paste()

    if raw == '':
        print("Clipboard is empty.")
    else:
        df = raw_to_df(raw)