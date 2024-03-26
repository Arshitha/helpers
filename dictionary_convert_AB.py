#!/usr/local/bin/python3
"""
Converts CTDB legends (generally) in BIDS valid JSON sidecar files.

@Authors: Arshitha Basavaraj, Eric Earl
@Date: 2023-11-04
"""
# imports
import json
from pathlib import Path

import pandas as pd

# file path handling
LEGENDS = [f for f in Path('.').glob(r'[A-Za-z]*[L,l]egend*.xlsx') if f.is_file()]
OUTPUT_DIR = Path('reformatted')
OUTPUT = OUTPUT_DIR.joinpath('participants.json')

# start with a single entry dictionary
d = {
    "participant_id": {
        "LongName": "Participant Identifier",
        "Description": "Unique BIDS identifier for the participant in this study."
    }
}
for legend in LEGENDS:
    df = pd.read_excel(legend, sheet_name=0)  # open each legend file and read the first sheet

    current = ''
    for i, row in df.iterrows():
        # detecting if on first line of data dictionary/legend
        if current == '':
            # start
            ShortName = row['QUESTION_NAME']
            LongName = row['QUESTION_NAME']
            current = ShortName

            if not pd.isna(row['QUESTION_TEXT']):
                Description = row['QUESTION_TEXT']
            else:
                Description = None

            Levels = None

        if not pd.isna(row['QUESTION_TEXT']):
            # write
            d[ShortName] = {}
            d[ShortName]['LongName'] = LongName

            if Description:
                d[ShortName]['Description'] = Description

            if Levels:
                d[ShortName]['Levels'] = Levels

            # reset
            ShortName = row['QUESTION_NAME']
            LongName = row['QUESTION_NAME']

            if not pd.isna(row['QUESTION_TEXT']):
                Description = row['QUESTION_TEXT']

            Levels = None

        if not Levels and not pd.isna(row['CODEVALUE']):
            Levels = {str(row['CODEVALUE']): str(row['DISPLAY'])}
        elif Levels and not pd.isna(row['CODEVALUE']):
            Levels[str(row['CODEVALUE'])] = str(row['DISPLAY'])

        # detecting if on last line of data dictionary/legend
        if i == df.shape[0] - 1:
            # write
            d[ShortName] = {}
            d[ShortName]['LongName'] = LongName
            if Description:
                d[ShortName]['Description'] = Description
            if Levels:
                d[ShortName]['Levels'] = Levels

with open(OUTPUT, 'w') as f:
    f.write(json.dumps(d, indent=4))
