import pandas as pd

def extract_tables(text):
    lines = text.split("\n")
    table = []
    for line in lines:
        if "," in line:
            table.append(line.split(","))
    if table:
        return pd.DataFrame(table)
    return None
