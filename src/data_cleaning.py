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


