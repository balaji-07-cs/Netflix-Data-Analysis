# ==================================================
# NETFLIX INTERACTIVE DASHBOARD
# STREAMLIT APPLICATION
# ==================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
import base64

from data_cleaning import load_data, clean_data


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Netflix Data Analysis",
    page_icon="🎬",
    layout="wide"
)


# ==================================================
# 2. PROJECT PATHS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "Dataset" / "Dataset.csv"

BACKGROUND_PATH = BASE_DIR / "Images" / "netflix_background.png"

LOGO_PATH = BASE_DIR / "Images" / "netflix_logo.png"


# ==================================================
# 3. CUSTOM DASHBOARD STYLING
# ==================================================

if BACKGROUND_PATH.exists():

    with open(BACKGROUND_PATH, "rb") as image_file:

        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.72),
                    rgba(0, 0, 0, 0.72)
                ),
                url("data:image/png;base64,{encoded_image}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stMain"] {{
            background-color: transparent;
        }}

        [data-testid="stSidebar"] {{
            background-color: rgba(15, 15, 15, 0.94);
        }}

        h1 {{
            color: #E50914;
            font-weight: bold;
        }}

        h2, h3 {{
            color: white;
        }}

        [data-testid="stMetric"] {{
            background-color: rgba(30, 30, 30, 0.90);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.10);
        }}

        .stDownloadButton button {{
            background-color: #E50914;
            color: white;
            border-radius: 8px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.warning("Background image not found. Check Images folder.")


# ==================================================
# 4. LOAD AND CLEAN DATA
# ==================================================

@st.cache_data
def get_data():

    df = load_data(DATASET_PATH)

    df_clean = clean_data(df)

    return df_clean


df_clean = get_data()


# ==================================================
# 5. DASHBOARD HEADER - LOGO AND TITLE
# ==================================================

col1, col2 = st.columns([1.5, 8.5])

with col1:

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            width=150
        )

    else:

        st.warning("Netflix logo not found.")


with col2:

    st.markdown(
        """
        <h1 style="
            color: #E50914;
            font-size: 38px;
            margin-top: 10px;
            margin-bottom: 0px;
            position: relative;
            left: 120px;
        ">
            CONTENT ANALYSIS DASHBOARD
        </h1>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
    <p style="
        color: #DDDDDD;
        font-size: 18px;
        text-align: center;
    ">
        Explore Netflix Movies, TV Shows and Content Insights
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# ==================================================
# 6. DASHBOARD FILTERS
# ==================================================

st.sidebar.title("🎬 Dashboard Filters")


# Content Type Filter

type_options = sorted(
    df_clean["type"].dropna().unique()
)

selected_type = st.sidebar.multiselect(
    "Select Content Type",
    options=type_options,
    default=type_options
)


# Content Rating Filter

rating_options = sorted(
    df_clean["rating"].dropna().unique()
)

selected_ratings = st.sidebar.multiselect(
    "Select Content Rating",
    options=rating_options,
    default=rating_options
)


# Release Year Filter

min_year = int(df_clean["release_year"].min())

max_year = int(df_clean["release_year"].max())

selected_years = st.sidebar.slider(
    "Select Release Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)


# Country Filter

country_options = sorted({

    country.strip()

    for countries in df_clean["country"].dropna()

    for country in countries.split(",")

    if country.strip()

})


selected_countries = st.sidebar.multiselect(
    "Select Country",
    options=country_options
)


# ==================================================
# 7. APPLY ALL FILTERS
# ==================================================

filtered_df = df_clean[

    (df_clean["type"].isin(selected_type)) &

    (df_clean["rating"].isin(selected_ratings)) &

    (df_clean["release_year"].between(
        selected_years[0],
        selected_years[1]
    ))

].copy()


# Apply Country Filter

if selected_countries:

    filtered_df = filtered_df[

        filtered_df["country"].apply(

            lambda countries: (

                pd.notna(countries) and

                any(

                    country.strip() in selected_countries

                    for country in countries.split(",")

                )

            )

        )

    ]

# ==================================================
# 8. NETFLIX CONTENT OVERVIEW
# ==================================================

st.subheader("Netflix Content Overview")

# ==================================================
# 9. NETFLIX CONTENT OVERVIEW - METRIC CARDS
# ==================================================

total_titles = len(filtered_df)

movie_count = (filtered_df["type"] == "Movie").sum()

tv_count = (filtered_df["type"] == "TV Show").sum()

movie_percentage = (
    (movie_count / total_titles) * 100 if total_titles > 0 else 0
)

tv_percentage = (
    (tv_count / total_titles) * 100 if total_titles > 0 else 0
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div style="
            background-color: rgba(25, 25, 25, 0.90);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            border-bottom: 4px solid #E50914;
        ">
            <h4 style="color: #E50914;">🎬 Total Titles</h4>
            <h1 style="color: white;">{total_titles:,}</h1>
            <p style="color: #CCCCCC;">100% of Content</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="
            background-color: rgba(25, 25, 25, 0.90);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            border-bottom: 4px solid #E50914;
        ">
            <h4 style="color: #E50914;">🍿 Movies</h4>
            <h1 style="color: white;">{movie_count:,}</h1>
            <p style="color: #CCCCCC;">{movie_percentage:.2f}% of Content</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="
            background-color: rgba(25, 25, 25, 0.90);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            border-bottom: 4px solid #E50914;
        ">
            <h4 style="color: #E50914;">📺 TV Shows</h4>
            <h1 style="color: white;">{tv_count:,}</h1>
            <p style="color: #CCCCCC;">{tv_percentage:.2f}% of Content</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()



# ==================================================
# 10. TOP 10 GENRES AND COUNTRIES
# ==================================================

col1, col2 = st.columns(2)


# Top 10 Genres

with col1:

    st.subheader("Top 10 Netflix Genres")

    genre_counts = (

        filtered_df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)

    )

    if not genre_counts.empty:

        st.bar_chart(genre_counts)

    else:

        st.info("No genre data available.")


# Top 10 Countries

with col2:

    st.subheader("Top 10 Countries")

    country_counts = (

        filtered_df["country"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)

    )

    if not country_counts.empty:

        st.bar_chart(country_counts)

    else:

        st.info("No country data available.")


st.divider()


# ==================================================
# 11. CONTENT RATING COMPARISON
# ==================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("Content Rating Comparison")

    rating_comparison = pd.crosstab(
        filtered_df["type"],
        filtered_df["rating"],
        normalize="index"
    ) * 100

    if not rating_comparison.empty:

        fig, ax = plt.subplots(figsize=(8, 5))

        rating_comparison.T.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Movies vs TV Shows Ratings")

        ax.set_xlabel("Content Rating")

        ax.set_ylabel("Percentage (%)")

        ax.tick_params(
            axis="x",
            rotation=45
        )

        ax.legend(title="Content Type")

        fig.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    else:

        st.info("No rating data available.")


# ==================================================
# 12. CONTENT ADDED OVER THE YEARS
# ==================================================

with col2:

    st.subheader("Content Added Over the Years")

    yearly_content = (

        filtered_df
        .dropna(subset=["date_added_year"])
        .groupby(["date_added_year", "type"])
        .size()
        .unstack(fill_value=0)

    )

    if not yearly_content.empty:

        fig, ax = plt.subplots(figsize=(8, 5))

        yearly_content.plot(
            kind="line",
            marker="o",
            ax=ax
        )

        ax.set_title("Netflix Content Added Each Year")

        ax.set_xlabel("Year")

        ax.set_ylabel("Number of Titles")

        ax.legend(title="Content Type")

        ax.grid(True)

        fig.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    else:

        st.info("No content addition data available.")


st.divider()


# ==================================================
# 13. MOVIE DURATION ANALYSIS
# ==================================================

st.subheader("Movie Duration Analysis")

movie_data = filtered_df[

    (filtered_df["type"] == "Movie") &
    (filtered_df["duration_number"].notna())

]

if not movie_data.empty:

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.hist(
        movie_data["duration_number"],
        bins=20,
        edgecolor="black"
    )

    ax.set_title("Distribution of Movie Durations")

    ax.set_xlabel("Duration (Minutes)")

    ax.set_ylabel("Number of Movies")

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

else:

    st.info("No movie duration data available.")


st.divider()


# ==================================================
# 14. DATASET PREVIEW
# ==================================================

st.subheader("Netflix Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)


# ==================================================
# 15. DOWNLOAD FILTERED DATASET
# ==================================================

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv_data,
    file_name="netflix_filtered_data.csv",
    mime="text/csv"
)


# ==================================================
# 16. PROJECT FOOTER
# ==================================================

st.divider()

st.html("""
<div style="
    text-align: center;
    color: #CCCCCC;
    padding: 25px;
    background-color: rgba(20, 20, 20, 0.90);
    border-radius: 12px;
    margin-top: 20px;
">

    <h3 style="color: #E50914;">
        🎬 Netflix Content Analysis Dashboard
    </h3>

    <p>
        Developed using Python | Pandas | Matplotlib | Streamlit
    </p>

    <p>
        Data Analytics Project - 2026
    </p>

</div>
""")