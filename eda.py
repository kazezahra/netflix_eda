import pandas as pd

# Load dataset
df = pd.read_csv("/home/pc-42/Downloads/netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

print(df.info())
print(df.describe())
print(df['type'].unique())  # Shows unique values in the 'type' column

import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x="type", data=df)
plt.title("Count of TV Shows and Movies")
plt.show()

df['release_year'].value_counts().sort_index().plot(kind='bar', figsize=(12,5))
plt.title("Number of Movies Released per Year")
plt.show()


