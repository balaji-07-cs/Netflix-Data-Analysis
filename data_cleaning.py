# ==========================================
# DATA CLEANING MODULE
# ==========================================

import pandas as pd


# Function to load the Netflix dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


# Function to clean the Netflix dataset
def clean_data(df):

    # Replace "Not Given" with missing values
    df = df.replace("Not Given", pd.NA)

    # Remove leading and trailing spaces from text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Convert date_added into datetime format
    df["date_added"] = pd.to_datetime(
        df["date_added"],
        errors="coerce"
    )

    # Extract year and month
    df["date_added_year"] = df["date_added"].dt.year
    df["date_added_month"] = df["date_added"].dt.month

    # Extract numeric duration
    df["duration_number"] = (
        df["duration"].str.extract(r"(\d+)").astype("Int64")
    )

    return df