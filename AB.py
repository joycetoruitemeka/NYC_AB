import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Cleaning the data
#Loading it
df = pd.read_csv("AB_NYC_2019.csv")

#Inspect the data
print(df.info())
print(df.describe())
print(df.head())

#Check for missing values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

#Identify duplicates
duplicates = df.duplicated()
print("Duplicated values:\n", duplicates)

#Identify outliers
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df["price"]< Q1 - 1.5 * IQR) | (df["price"] > Q3 + 1.5 * IQR)]
print("Outliers:\n", outliers)

#Check for valid dates
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

#Drop missing columns
df_cleaned = df.dropna()

#Drop duplicates
df_cleaned = df.drop_duplicates()

#Standardize the text to check for typos
df_cleaned['neighbourhood'] = df_cleaned['neighbourhood'].str.lower().str.strip()
df_cleaned['neighbourhood_group'] = df_cleaned['neighbourhood_group'].str.lower().str.strip()
df_cleaned['host_name'] = df_cleaned['host_name'].str.lower().str.strip()
print(df_cleaned['neighbourhood'].value_counts())

#Check for invalid numbers or zeros
print(df_cleaned[df_cleaned['price'] <= 0])
print(df_cleaned[df_cleaned['minimum_nights'] <= 0])

df_cleaned = df_cleaned[df_cleaned['price'] > 0]

#Check for valid dates
#df_cleaned['last_review'] = pd.to_datetime(df_cleaned['last_review'], errors='coerce')

#Top 10 hosts
top_hosts = df_cleaned['host_id'].value_counts().head(10)
print("Top 10 hosts by listing count:\n", top_hosts)

#Average price per neighborhood group
avg_price_neighborhood_group = df_cleaned.groupby('neighbourhood_group')['price'].mean()
print(avg_price_neighborhood_group)

#Average price per neighborhood
avg_price_neighborhood = df_cleaned.groupby('neighbourhood')['price'].mean().sort_values(ascending=False)

#Price Distribution
sns.histplot(df_cleaned['price'], bins=50)
plt.title('Price Distribution')

#Listings per neighborhood
sns.countplot(data=df_cleaned, x='neighbourhood_group')
plt.title('Listings by Borough')

#Average price per room type
sns.barplot(data=df_cleaned, x='room_type', y='price')
plt.title('Average price per room type')

#Export to a csv file
df_cleaned.to_csv('clean_ab_nyc.csv', index=False) 