import pandas as pd
import os

def export_to_excel(data, path="data/exported_data.xlsx"):
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_excel(path, index=False)
    return path
