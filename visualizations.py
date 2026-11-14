# ==========================================
# NETFLIX DATA VISUALIZATION MODULE
# ==========================================

import matplotlib.pyplot as plt
import pandas as pd
import os


# Create folder if it doesn't exist
os.makedirs("Visualizations", exist_ok=True)


# 1. Movies vs TV Shows Pie Chart
def plot_content_type(df):

    content_counts = df["type"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        content_counts,
        labels=content_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Netflix Movies vs TV Shows Distribution")
    plt.tight_layout()

    plt.savefig("Visualizations/content_type_pie.png", dpi=300)
    plt.show()
    plt.close()


# 2. Top 10 Genres Bar Chart
def plot_top_genres(df):

    genre_counts = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    genre_counts.sort_values().plot(kind="barh")

    plt.title("Top 10 Netflix Genres")
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")

    plt.tight_layout()

    plt.savefig("Visualizations/top_10_genres.png", dpi=300)
    plt.show()
    plt.close()


# 3. Yearly Content Addition Line Chart
def plot_content_added(df):

    yearly_content = (
        df.groupby("date_added_year")["show_id"].count()
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        yearly_content.index,
        yearly_content.values,
        marker="o"
    )

    plt.title("Netflix Content Added Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles Added")
    plt.grid(True)

    plt.tight_layout()

    plt.savefig("Visualizations/content_added_yearly.png", dpi=300)
    plt.show()
    plt.close()


# 4. Content Rating Bar Chart
def plot_content_ratings(df):

    rating_counts = df["rating"].value_counts()

    plt.figure(figsize=(12, 6))

    rating_counts.plot(kind="bar")

    plt.title("Netflix Content Rating Distribution")
    plt.xlabel("Content Rating")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("Visualizations/content_ratings.png", dpi=300)
    plt.show()
    plt.close()


# 5. Movie Duration Histogram
def plot_movie_duration(df):

    movie_data = df[df["type"] == "Movie"]

    plt.figure(figsize=(10, 6))

    plt.hist(
        movie_data["duration_number"].dropna(),
        bins=30,
        edgecolor="black"
    )

    plt.title("Distribution of Netflix Movie Durations")
    plt.xlabel("Movie Duration (Minutes)")
    plt.ylabel("Number of Movies")

    plt.tight_layout()

    plt.savefig("Visualizations/movie_duration.png", dpi=300)
    plt.show()
    plt.close()


# 6. Rating Comparison Chart
def plot_rating_comparison(df):

    rating_comparison = pd.crosstab(
        df["rating"],
        df["type"]
    )

    rating_comparison.plot(
        kind="bar",
        figsize=(12, 6)
    )

    plt.title("Content Rating Comparison: Movies vs TV Shows")
    plt.xlabel("Content Rating")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45)
    plt.legend(title="Content Type")

    plt.tight_layout()

    plt.savefig("Visualizations/rating_comparison.png", dpi=300)
    plt.show()
    plt.close()


# 7. Function to Execute All Visualizations
def run_visualizations(df):

    print("\n========== CREATING VISUALIZATIONS ==========")

    plot_content_type(df)
    plot_top_genres(df)
    plot_content_added(df)
    plot_content_ratings(df)
    plot_movie_duration(df)
    plot_rating_comparison(df)

    print("\nAll six visualizations created successfully!")