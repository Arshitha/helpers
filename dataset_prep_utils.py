import msoffcrypto
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd


def run(cmdstr):
    p = subprocess.run(cmdstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', shell=True)
    return p.stdout


def set_participant_contributions(files_list, inventory_df, column_name):
    prev_rowidx = inventory_df.shape[0]
    for f in files_list:
        curr_rowidx = prev_rowidx + 1
        pid = f.parts[-3]
        if not inventory_df.loc[inventory_df['participant_id'] == pid, 'participant_id'].values:
            inventory_df.at[rowidx, 'participant_id'] = pid
            inventory_df.at[rowidx, column_name] = 1
            prev_rowidx = curr_rowidx
        else:
            inventory_df.loc[inventory_df['participant_id'] == pid, column_name] = 1


def set_tab_data_contributions(phenotype_files):
  for pf in phenotype_files:
    df = pd.read_csv(pf, sep='\t', keep_default_na=False)
    for idx, row in df.iterrows():
        # remove rows with all n/a's except participant_id
        uniq_elements = set(row[1:])
        if len(uniq_elements) == 1 and list(uniq_elements)[0] == 'n/a':
            pass
        else:
            pid = row['participant_id']
            if not actual_ptsv_df.loc[actual_ptsv_df['participant_id'] == pid, 'participant_id'].values:
                actual_ptsv_df.at[rowidx, 'participant_id'] = pid
                actual_ptsv_df.at[rowidx, pf.name.split('.')[0]] = 1
                rowidx += 1
            else:
                actual_ptsv_df.loc[actual_ptsv_df['participant_id'] == pid, pf.name.split('.')[0]] = 1
  

def replace_nans(df, replacement_str):
    for col in df.columns:
        for idx, val in df[col].items():
            if val in ['NA', '', np.NaN]:
                if not replacement_str:
                    df.at[idx, col] = 'n/a'
                else:
                    df.at[idx, col] = int(replacement_str)
    return df


## Reference: https://stackoverflow.com/a/68867250/4393932
def decrypt_workbook(filepath, passwrd):
    decrypted_workbook = io.BytesIO()
    with open(filepath, 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=passwrd)
        office_file.decrypt(decrypted_workbook)
    return decrypted_workbook
