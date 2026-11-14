# ==========================================
# NETFLIX DATA ANALYSIS MODULE
# ==========================================

import pandas as pd


# 1. Content Type Analysis
def analyze_content_type(df):

    print("\n========== CONTENT TYPE ANALYSIS ==========")

    content_counts = df["type"].value_counts()

    print(content_counts)

    content_percentage = df["type"].value_counts(normalize=True) * 100

    print("\nContent Type Percentage:")
    print(content_percentage.round(2))


# 2. Country Analysis
def analyze_countries(df):

    print("\n========== COUNTRY ANALYSIS ==========")

    country_counts = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
    )

    print("\nTop 10 Countries:")
    print(country_counts.head(10))


# 3. Rating Analysis
def analyze_ratings(df):

    print("\n========== CONTENT RATING ANALYSIS ==========")

    rating_counts = df["rating"].value_counts()

    print(rating_counts.head(10))


# 4. Genre Analysis
def analyze_genres(df):

    print("\n========== GENRE ANALYSIS ==========")

    genre_counts = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
    )

    print("\nTop 10 Genres:")
    print(genre_counts.head(10))


# 5. Content Added Over Time
def analyze_content_added(df):

    print("\n========== CONTENT ADDED ANALYSIS ==========")

    yearly_content = df["date_added_year"].value_counts().sort_index()

    print(yearly_content)


# 6. Movie Duration Analysis
def analyze_movie_duration(df):

    print("\n========== MOVIE DURATION ANALYSIS ==========")

    movie_data = df[df["type"] == "Movie"]

    print("Average Movie Duration:",
          round(movie_data["duration_number"].mean(), 2), "minutes")

    print("Shortest Movie:",
          movie_data["duration_number"].min(), "minutes")

    print("Longest Movie:",
          movie_data["duration_number"].max(), "minutes")


# 7. TV Show Season Analysis
def analyze_tv_shows(df):

    print("\n========== TV SHOW ANALYSIS ==========")

    tv_data = df[df["type"] == "TV Show"]

    print("Average Number of Seasons:",
          round(tv_data["duration_number"].mean(), 2))

    print("Maximum Seasons:",
          tv_data["duration_number"].max())


# 8. Main Analysis Function
def run_analysis(df):

    analyze_content_type(df)

    analyze_countries(df)

    analyze_ratings(df)

    analyze_genres(df)

    analyze_content_added(df)

    analyze_movie_duration(df)

    analyze_tv_shows(df)