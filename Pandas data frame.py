import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Reading from a CSV file (commented out since we don't have a file in this example)
# df = pd.read_csv('filename.csv')

# Viewing the DataFrame
print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nRandom 5 rows:\n", df.sample(3))  # Sample size reduced for demonstration
print("\nDataFrame Info:\n", df.info())
print("\nStatistical Summary:\n", df.describe())

# Selecting data
ages = df['Age']
print("\nAges column:\n", ages)

name_age = df[['Name', 'Age']]
print("\nName and Age columns:\n", name_age)

first_row = df.iloc[0]
print("\nFirst row:\n", first_row)

first_three_rows = df.iloc[:3]
print("\nFirst three rows:\n", first_three_rows)

over_30 = df[df['Age'] > 30]
print("\nRows where age is over 30:\n", over_30)

# Adding and modifying columns
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with Salary column added:\n", df)

df['Age'] = df['Age'] + 1
print("\nDataFrame with Age column modified:\n", df)

# Handling missing data
# Adding a row with missing values for demonstration
df.loc[3] = ['David', None, None, None]
print("\nDataFrame with missing values:\n", df)

df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:\n", df_filled)

df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_dropped)

# Grouping and aggregating data
grouped = df.groupby('City').mean()
print("\nGrouped by City and averaged:\n", grouped)

# Merging and joining DataFrames
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'City': ['New York', 'Los Angeles']
})

merged_df = pd.merge(df1, df2, on='Name')
print("\nMerged DataFrame:\n", merged_df)

# Saving to a CSV file (output is disabled in this notebook environment)
# df.to_csv('output.csv', index=False)
