# imports
import json
from pathlib import Path

import pandas

# TODO: remove hardcoding
# file path handling
INPUT = Path('pine_group/CogQuad Legends - EE update.xlsx')
OUTPUT_DIR = Path('pine_group')

# TODO: read all the sheets but only parse sheetnames with "Legend/legend" in them
all = pandas.read_excel(INPUT, sheet_name=None)

for sheet in all:
    sheetname = str(sheet)
    df = all[sheetname]
    OUTPUT = OUTPUT_DIR.joinpath(sheetname.rstrip(" Legend").replace(" ", "_") + '.json')

    # open the output file for writing
    with open(OUTPUT, 'w') as f:
        # TODO: put this in dictionary indexing notation
        # start with a single entry dictionary
        d = {
            "participant_id": {
                "LongName": "Participant Identifier",
                "Description": "Unique BIDS identifier for the participant in this study."
            }
        }

        current = ''  # intialized for every new sheet
        for i, row in df.iterrows():
            # detecting if on first line of data dictionary/legend
            if current == '':
                # start
                ShortName = row['QUESTION_ALIAS']
                LongName = row['QUESTION_NAME']
                current = ShortName

                if not pandas.isna(row['QUESTION_TEXT']):
                    Description = row['QUESTION_TEXT']
                else:
                    Description = None

                Levels = None

            elif not pandas.isna(row['QUESTION_TEXT']):
                # write
                d[ShortName] = {}
                d[ShortName]['LongName'] = LongName

                if Description:
                    d[ShortName]['Description'] = Description

                if Levels:
                    d[ShortName]['Levels'] = Levels

                # reset
                ShortName = row['QUESTION_ALIAS']
                LongName = row['QUESTION_NAME']

                if not pandas.isna(row['QUESTION_TEXT']):
                    Description = row['QUESTION_TEXT']

                Levels = None

            if not Levels and not pandas.isna(row['CODEVALUE']):
                Levels = {str(row['CODEVALUE']): str(row['DISPLAY'])}
            elif Levels and not pandas.isna(row['CODEVALUE']):
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
