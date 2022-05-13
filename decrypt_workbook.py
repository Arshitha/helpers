import msoffcrypto
from pathlib import Path
import pandas as pd

## Reference: https://stackoverflow.com/a/68867250/4393932

def decrypt_workbook(filepath, passwrd):
    decrypted_workbook = io.BytesIO()
    with open(filepath, 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=passwrd)
        office_file.decrypt(decrypted_workbook)
    return decrypted_workbook
