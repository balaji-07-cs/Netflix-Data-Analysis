# ==========================================
# NETFLIX DATA ANALYSIS PROJECT
# MAIN FILE
# ==========================================


# Import required functions
from data_cleaning import load_data, clean_data
from data_analysis import run_analysis
from visualizations import run_visualizations


# 1. Load Dataset
df = load_data("Dataset/Dataset.csv")

print("Original Dataset Shape:", df.shape)


# 2. Clean Dataset
df_clean = clean_data(df)

print("Cleaned Dataset Shape:", df_clean.shape)


# 3. Perform Data Analysis
run_analysis(df_clean)


# 4. Create Visualizations
run_visualizations(df_clean)


print("\n========== PROJECT EXECUTION COMPLETED ==========")