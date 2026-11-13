Netflix Data Analysis Project

📌 Project Overview

This project focuses on exploring and analysing Netflix movies and TV shows using Python. The goal is to understand the content available on Netflix through data cleaning, exploratory data analysis (EDA), statistical summaries, and visualisations.

The project uses Python libraries to discover patterns and insights related to content types, countries, release years, ratings, genres, and durations.

🎯 Project Objectives

- Load and understand the Netflix dataset.
- Clean and preprocess the data.
- Identify missing values and duplicate records.
- Analyse Movies and TV Shows.
- Explore content distribution across countries.
- Analyse release years and Netflix content addition dates.
- Study content ratings and genres.
- Analyse movie durations and TV show seasons.
- Create meaningful visualisations.
- Build an interactive dashboard using Streamlit.

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook / VS Code
- Git and GitHub

📂 Project Structure

text

Netflix-Data-Analysis/
│
├── Dataset/
│   └── Dataset.csv
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore


Note:  The dataset is stored locally and is not included in the GitHub repository.

📊 Dataset Information

- Total Records: 8,790
- Total Columns: 10
- Movies: 6,126
- TV Shows: 2,664

Dataset Columns

- show_id
- type
- title
- director
- country
- date_added
- release_year
- rating
- duration
- listed_in

🧹 Data Cleaning

The following cleaning operations have been performed:

- Checked dataset dimensions and column information.
- Identified missing values.
- Replaced `"Not Given"` placeholders with missing values.
- Checked duplicate records and duplicate show IDs.
- Standardised content types and ratings.
- Converted `date_added` into datetime format.
- Extracted year and month from the date column.
- Extracted numerical values from the duration column.

📈 Exploratory Data Analysis (EDA)

The following analyses have been completed:

1. Content Type Analysis
2. Country-wise Content Analysis
3. Release Year Analysis
4. Content Rating Analysis
5. Genre Analysis
6. Content Added Over Time
7. Movie Duration Analysis
8. TV Show Seasons Analysis

🔍 Key Findings

- Netflix has 6,126 Movies and 2,664 TV Shows in the dataset.
- No duplicate full records or duplicate show IDs were found.
- TV-MA is the most common content rating, with 3,205 titles.
- International Movies is the most frequently listed genre, with 2,752 entries.
- 2019 had the highest number of content additions, with 2,016 titles.
- July had the highest number of additions when all available years were combined, with 827 titles.
- The average movie duration is approximately 99.58 minutes.
- The average number of seasons for TV Shows is approximately 1.75.
- Grey's Anatomy has the highest number of seasons in the dataset, with 17.

🚀 Project Progress

- [x] Dataset loading and inspection
- [x] Missing value analysis
- [x] Data cleaning
- [x] Content type analysis
- [x] Country analysis
- [x] Release year analysis
- [x] Content rating analysis
- [x] Genre analysis
- [x] Content added over time analysis
- [x] Movie duration analysis
- [x] TV show seasons analysis
- [ ] Business insights
- [ ] Advanced data analysis
- [ ] Final visualisations
- [ ] Streamlit dashboard development
- [ ] Project documentation and presentation

📌 Current Status

Data cleaning and the initial exploratory data analysis have been completed. The next phase will focus on extracting business insights, improving visualisations, and developing an interactive Streamlit dashboard.

👨‍💻 Author

Balaji B
