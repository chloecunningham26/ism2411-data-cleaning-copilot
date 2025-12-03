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


# This function handles missing values in the price and quantity columns
def handle_missing_values(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Handle missing values in the dataset.
    - Fill missing prices with the median price.
    - Fill missing quantities with zero.
    """
    if 'price' in df.columns:
        median_price = df['price'].median()
        df['price'] = df['price'].fillna(median_price)
    if 'quantity' in df.columns:
        df['quantity'] = df['quantity'].fillna(0)
    return df



# This function removes rows with invalid data such as negative prices or quantities
def remove_invalid_rows(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove rows with invalid data.
    - Remove rows with negative prices or quantities.
    """
    if 'price' in df.columns:
        df = df[df['price'] >= 0]
    if 'quantity' in df.columns:
        df = df[df['quantity'] >= 0]
    return df   