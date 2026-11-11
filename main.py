import pandas as pd

# Load the Netflix dataset
df = pd.read_csv("Dataset/Dataset.csv")

# Display the first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# Display data information
print("\nData Information:")
df.info()

# display Missing Values
print("\n Missing Values:")
print(df.isnull().sum())

# display duplicate values
print("\n Duplicate Values:")
print(df.duplicated().sum())

#count movies and tv shows
print("\n Count of Movies and TV Shows:")
print(df['type'].value_counts())

#Check Placeholder values in important columns
print("\n Director placeholder values:")
print(df['director'].value_counts().head(10))

print("\n country placeholder values:")
print(df['country'].value_counts().head(10))

print("\n rating placeholder values:")
print(df['rating'].value_counts().head(10))

#copy of the original dataset
df_clean = df.copy()

#Replace placeholder values with actual missing values
df_clean.replace("Not Given", pd.NA, inplace=True)

#check for missing values after replacement
print("\n Missing Values after replacement:")
print(df_clean.isnull().sum())

# Check duplicate show IDs
duplicate_ids = df_clean["show_id"].duplicated().sum()

print("\nDuplicate Show IDs:")
print(duplicate_ids)

# Standardise content types
df_clean["type"] = df_clean["type"].str.strip().str.casefold()

df_clean["type"] = df_clean["type"].replace({
    "movie": "Movie",
    "tv show": "TV Show"
})

# Standardise ratings
df_clean["rating"] = df_clean["rating"].str.strip().str.upper()

# Check results
print(df_clean["type"].value_counts())
print(df_clean["rating"].value_counts())

# Convert date_added into datetime format
df_clean["date_added"] = pd.to_datetime(
    df_clean["date_added"],
    errors="coerce"
)

# Check the result
print("\nDate Added Information:")
print(df_clean["date_added"].dtype)

print("\nFirst 5 Dates:")
print(df_clean["date_added"].head())

# Extract year
df_clean["date_added_year"] = df_clean["date_added"].dt.year

# Extract month
df_clean["date_added_month"] = df_clean["date_added"].dt.month

# Display results
print("\nDate Added Year:")
print(df_clean[["title", "date_added", "date_added_year"]].head())

print("\nDate Added Month:")
print(df_clean[["title", "date_added", "date_added_month"]].head())

# Extract numerical duration
df_clean["duration_number"] = (
    df_clean["duration"].str.extract(r"(\d+)").astype("Int64")
)

# Display results
print("\nDuration Analysis:")
print(df_clean[["title", "type", "duration", "duration_number"]].head(10))