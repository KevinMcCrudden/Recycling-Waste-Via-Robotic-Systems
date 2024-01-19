import pandas as pd

# Read the CSV file
df = pd.read_csv('22-23_WM_Recycling_Data.csv')

# Assuming your CSV columns are named 'Month' and 'Year'
# Convert 'Year' and 'Month' columns to strings to ensure correct sorting
df['YEAR'] = df['YEAR'].astype(str)
df['MONTH'] = df['MONTH'].astype(str)

# Create a new column 'YearMonth' by concatenating 'Year' and 'Month'
df['YearMonth'] = df['YEAR'] + df['MONTH']

# Convert 'TONNAGE' column to numeric (assuming it contains numeric values)
df['TONNAGE'] = pd.to_numeric(df['TONNAGE'], errors='coerce')

# Sort the DataFrame by 'YearMonth'
df.sort_values(by='YearMonth', inplace=True)

# Create new columns for month totals
for month in range(1, 13):
    month_str = str(month)
    month_total_column = f'Month_{month_str}_Total'
    df[month_total_column] = df[df['MONTH'] == month_str]['TONNAGE'].sum()

# Drop the temporary 'YearMonth' column if you don't need it anymore
df.drop('YearMonth', axis=1, inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('modified_csv_file.csv', index=False)
