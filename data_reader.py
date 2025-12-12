import pandas as pd
import os

def read_credentials(path="data/credentials.xlsx"):
    if not os.path.exists(path):
        return []
    df = pd.read_excel(path)
    return df.to_dict(orient="records")

def read_transfers(path="data/transfer_data.xlsx"):
    if not os.path.exists(path):
        return []
    df = pd.read_excel(path)
    return df.to_dict(orient="records")
