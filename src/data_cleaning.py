"""
This script loads a raw sales dataset, cleans common data quality issues,
and saves a cleaned version for analysis and reporting.
"""

import pandas as pd
# This function loads the raw CSV file into a pandas DataFrame

def load_data(file_path: str):
    """
    Load the raw sales data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df

# This function standardizes column names by making them lowercase and using underscores
def clean_column_names(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Standardize column names to lowercase with underscores.
    """
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w\s]", "", regex=True)
    )
    return df
