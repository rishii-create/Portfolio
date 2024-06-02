# -*- coding: utf-8 -*-
"""A2_25105230_Python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1347PLAEKzNS2iGokS0NsgtDpmaVPiKtX

```
# This is formatted as code
```

**Top European Soccer League from Year 2014-2019- Data Analysis**
---

Part 1- Data Loading

---


Part 2- Data Cleaning and Verification

---


Part 3- Data Exploration

```
```

# Part 1: Data Loading

## 1.1 Mount data to google drive

> Add blockquote
"""

#Mount the raw data to googledrive
#Data from Kaggle https://www.kaggle.com/datasets/slehkyi/extended-football-stats-for-european-leagues-xg
from google.colab import drive
drive.mount('/content/drive')

"""## 1.2 Import pandas library, Read CSV and Show few Rows"""

#import pandas library for data analysis
#import csv file for analysis
import pandas as pd
import csv
csv_file_path = '/content/drive/MyDrive/43031/raw_data_python/understat.com.csv'
data = pd.read_csv(csv_file_path)
# Display the first few rows of the dataframe
data.head()

"""```
# This is formatted as code
```

# Part 2- Data Cleaning and Verification (Lowercase, Filter, Missing values, Outliers, Duplicates)

## 2.1 Data Information (Data types, Null, Column Headers)
"""

#Data information( Column Name, Type, Null Values)
print(data.info())

"""**`There were no missing values in the dataset. However, there is missing variable name, and data type needs to be changed in few instances.`**

## 2.2 Count Number of Rows and Column
"""



"""## 2.2 Datapoints into lowercase transformation"""

#Categorical datatypes changed into lowercase....
string_columns = data.select_dtypes(include=['object']).columns

for column in string_columns:
    data[column] = data[column].str.lower()

"""## 2.3 Rename missing headers"""

#adding headers for missing headers
data.rename(columns={'Unnamed: 0': 'league', 'Unnamed: 1': 'year'}, inplace=True)
print(data.columns)

"""## 2.4 Data Type Change- Integer Type to Date Type"""

#Changed data type of year from integer to date
data['year'] = data['year'].astype(str)

"""## 2.5 Filter Data for the analysis"""

# Filter the data for top 4 teams as the data includes the all the 20 teams for each league
top_teams = data[(data['position'] <= 4)]
top_teams = data[(data['position'] <= 4)]

"""[link text](https://)## 2.6 Count Number of Column and Rows after Filtering"""

# Count rows and columns of new dataset top_teams after filterings
num_rows = top_teams.shape[0]
num_columns = top_teams.shape[1]

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

"""## 2.7 Formatting Float (2 Decimal Place)"""

# formatting details
def format_floats(top_teams):
    for col in top_teams.select_dtypes(include=['float64']).columns:
        top_teams[col] = top_teams[col].round(2)
    return top_teams

# Applying the formatting
top_teams = format_floats(top_teams=top_teams.copy())

"""***A copy of data is created after cleaning the data as a top_teams.copy***

## 2.8 Display Top and Bottom Five Rows
"""

# Display the top 5 rows
print("Top 5 rows:")
print(top_teams.head())

# Display the bottom 5 rows
print("\nBottom 5 rows:")
print(top_teams.tail())

"""## 2.9 Identify and Display Duplicate Rows and Columns"""

# Identify duplicate rows
duplicate_rows = top_teams[top_teams.duplicated()]

# Display duplicate rows'
duplicate_rows = top_teams[data.duplicated()]
print(duplicate_rows.shape)
print("Duplicate Rows:")
print(duplicate_rows)

# Identify duplicate columns
duplicate_columns = top_teams.transpose().duplicated()
print(duplicate_columns)
duplicate_columns = top_teams.columns[top_teams.columns.duplicated()]

# Display duplicate columns
print("Duplicate Columns:")
print(duplicate_columns)

"""## 2.10 Outliers Using Box Plot"""

import matplotlib.pyplot as plt
import pandas as pd


# Numerical columns excluding 'year' (As 'year' is the string column)
numerical_columns = ['matches', 'wins', 'draws', 'loses', 'scored', 'missed', 'pts', 'xG', 'xG_diff',
                'npxG', 'xGA', 'xGA_diff', 'npxGA', 'npxGD', 'ppda_coef', 'oppda_coef',
                'deep', 'deep_allowed', 'xpts', 'xpts_diff']
# Box plots
plt.figure(figsize=(12, 6)) # Adjust figure size as needed
top_teams[numerical_columns].boxplot()
plt.xticks(rotation=45, ha='right')
plt.title('Box Plots for Numerical Columns')
plt.tight_layout()
plt.show()

"""***Outliers are present across the variables, except position, wins, scored, missed, points, expected goals without penalty and own goal(npxG), expected goals conceded(xGa), and expected points(xpts). Based on the preliminary analysis and the type of analysis, outliers will be removed and analysed. However more careful assesement and handling of the outliers is needed. ***

## 2.11 Display Final Dataset
"""

#Final Dataset with clear formats removing insignificant variable
top_teams = top_teams.copy()


#displaying top five rows
print(top_teams.head())

#Treatment 1
#Question: Remove all the rows with outliers
# Function to remove outliers from all numeric attributes
print(top_teams.shape)

import numpy as np

def remove_outliers(top_teams):
    top_teams_clean = top_teams.copy()
    for col in top_teams_clean.select_dtypes(include=["number"]).columns:
        Q1 = np.percentile(top_teams_clean[col], 25)
        Q3 = np.percentile(top_teams_clean[col], 75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        top_teams_clean = top_teams_clean[(top_teams_clean[col] >= lower_bound) & (top_teams_clean[col] <= upper_bound)]
    return top_teams_clean

# Remove outliers from DataFrame
top_teams_clean = remove_outliers(top_teams)
print(top_teams_clean.shape)

import matplotlib.pyplot as plt
import pandas as pd


# Numerical columns excluding 'year' (As 'year' is the string column)
numerical_columns = ['matches', 'wins', 'draws', 'loses', 'scored', 'missed', 'pts', 'xG', 'xG_diff',
                'npxG', 'xGA', 'xGA_diff', 'npxGA', 'npxGD', 'ppda_coef', 'oppda_coef',
                'deep', 'deep_allowed', 'xpts', 'xpts_diff']
# Box plots
plt.figure(figsize=(12, 6)) # Adjust figure size as needed
top_teams_clean[numerical_columns].boxplot()
plt.xticks(rotation=45, ha='right')
plt.title('Box Plots for Numerical Columns')
plt.tight_layout()
plt.show()

"""`*A final dataset is copied into top_teams_fina; which is furthered formatted to two decimal place and lastly the top 5 rows is displayed*`

---

# Part 3- Data Exploration

---

## 3.1 Sum and Average of Key Metrics of Football Performance
"""

# Identify numerical columns (as 'team' is your categorical column)

numeric_cols = ['matches', 'wins', 'draws', 'loses', 'scored', 'missed', 'pts', 'xG', 'xG_diff',
                'npxG', 'xGA', 'xGA_diff', 'npxGA', 'npxGD', 'ppda_coef', 'oppda_coef',
                'deep', 'deep_allowed', 'xpts', 'xpts_diff']

#creating table for sum and average of key metrics
from tabulate import tabulate

results = []
for metrics in numeric_cols:
  metrics_sum = top_teams_clean[metrics].sum()
  metrics_avg = top_teams_clean[metrics].mean()
  results.append([metrics, f"{metrics_sum:.2f}", f"{metrics_avg:.2f}"])  # Formatting 2 decimal place

print("Sum and Average of Metrics")
print(tabulate(results, headers=['Metrics', 'Sum', 'Average'], tablefmt='psql'))

"""36877888888## 3.2 Summary Statistics"""

# Summary statistics
summary_stat = top_teams_clean.drop(['year', 'position', 'matches'], axis=1).describe().round(2)

# Display Of the table
print("\nSummary statistics ")
print(summary_stat.to_string())

"""## 3.3 Correlation Heatmap"""

# Produce a coorelation matrix of the relevent variables
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Import Seaborn


corr_matrix = top_teams_clean[numeric_cols].corr()
plt.figure(figsize=(14, 14))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

"""## 3.4 Comparision"""

import pandas as pd

# Assuming 'league' is a column in your 'top_teams_final' DataFrame
goals_per_league = top_teams_clean.groupby('league')['scored'].sum()

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
goals_per_league.plot(kind='bar')
plt.xlabel('League')
plt.ylabel('Total Goals Scored')
plt.title('Total Goals Scored by Top Four On Each League')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels if needed
plt.tight_layout()  # Improve layout
plt.show()



import pandas as pd

def calculate_goals_by_top_positions(df):
    """Calculates total goals scored by the top 4 teams for each league.

    Args:
        df (pandas.DataFrame): The DataFrame containing league, position, and goals data.

    Returns:
        pandas.DataFrame: A DataFrame with 'league' column as index, and columns 'Position 1',
                          'Position 2', 'Position 3', 'Position 4', containing goal totals.
    """

    result = df.groupby(['league', 'position'])['scored'].sum()
    return result.unstack().iloc[:, :4]  # Focus on top 4 positions

# Apply the calculation
top_4_goals_per_league = calculate_goals_by_top_positions(top_teams_clean.copy())
print(top_4_goals_per_league)

import pandas as pd

# ... (Your code for the 'calculate_goals_by_top_positions' function)

top_4_goals_per_league = calculate_goals_by_top_positions(top_teams_clean.copy())

# Output Formatting
for position in range(1, 5):
    print(f"\nPosition {position}:")
    for league, goals in top_4_goals_per_league.loc[:, position].items():
        print(f"{league}: ({goals} Scored)")

import matplotlib.pyplot as plt

# ... Your code (calculate_goals_by_top_positions function and output formatting)

# ... (Data preparation same as before)

# Visualization
plt.figure(figsize=(12, 8))

num_positions = len(data_for_plot)
bar_width = 0.8 / num_positions
x_positions = np.arange(len(top_4_goals_per_league))

for i, (goals, labels) in enumerate(data_for_plot):
    offset = (i - (num_positions - 1) / 2) * bar_width
    bars = plt.bar(x_positions + offset, goals, width=bar_width, label=f'Position {i+1}', align='center', alpha=0.8, edgecolor='black')

    # Add data labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

plt.xlabel('League')
plt.ylabel('Goals Scored')
plt.title('Goals Scored by League and Position (Top 4)')
plt.xticks(x_positions, labels, rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()