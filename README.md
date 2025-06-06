# NYC Airbnb Listings Analysis (2019)

## Project Overview

This project analyzes Airbnb listings across New York City using a dataset from 2019. The goal was to explore pricing trends, listing availability, review behavior, and neighborhood-level patterns to better understand the dynamics of the short-term rental market in NYC.

I used **Python** for data cleaning and exploratory analysis, and **Tableau** to design an interactive dashboard that visualizes key trends across boroughs and room types.

---

## Tools & Technologies

- **Python (Pandas, Seaborn, Matplotlib)** for cleaning and EDA  
- **Tableau Public** for data visualization  

---

## Files Included

- `AB_NYC_2019.csv` – Raw dataset from [Kaggle](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
- `nyc_airbnb_cleaning_script.py` – Python script for data cleaning and prep
- `clean_ab_nyc.csv` – Cleaned version of the dataset used in Tableau
- `README.md` – You’re here!

---

## Dashboard Visualizations

🔗 **[View Dashboard Here](https://public.tableau.com/views/NYC_17491894898340/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)** 

The dashboard includes the following charts:

1. **Average Price by Borough**  
   Visualizes average Airbnb prices by NYC borough, noting that neighborhoods like Neponsit and Willowbrook have high averages but low listing counts.

2. **Room Type Popularity Based on Availability**  
   Compares how often each room type is available, showing a near-equal split between private rooms and entire homes/apartments.

3. **Do Higher-Priced Listings Get More Reviews?**  
   Explores the relationship between listing price and review count across different room types.

4. **Number of Listings by Borough**  
   Shows boroughs with the most listings, highlighting the Financial District as a hotspot.

---

## Key Insights

- **High Prices ≠ Low Reviews**: Higher-priced listings, especially entire homes/apartments, still attract significant reviews.
- **Private Rooms Dominate Availability**: They slightly edge out entire homes, suggesting they’re a popular choice for travelers.
- **Financial District is a Listing Hub**: With over 69,000 listings, it’s a central node in NYC’s Airbnb market.
- **Neighborhood Size Matters**: Some expensive neighborhoods have few listings, so averages may be skewed.

---

## Data Cleaning Summary

Performed in Python:
- Removed duplicates and rows with missing critical values
- Filtered out listings with prices ≤ 0
- Standardized neighborhood and host text data
- Validated and cleaned date formats in the `last_review` column
