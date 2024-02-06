import pandas as pd
from pandas.tseries.offsets import MonthEnd
from calendar import month_name
import math

class MyClass:
    def __init__(self):
        # Initialize the class with some variables from matlab
        self.test = 3

    def convert_to_month_names(self, raw_csv_file):
        # Define a dictionary to map integers to month names
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Define a dictionary to map integers to month names
        month_mapping = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        # Convert 'MONTH' column to its corresponding month names
        df['MONTH_STRING'] = df['MONTH'].apply(lambda month: month_mapping.get(month, 'Invalid Month'))

        # Save the updated DataFrame to a new CSV file
        new_file = raw_csv_file.replace('.csv', '_month.csv')
        df.to_csv(new_file, index=False)

        return new_file
    
    def sorter(self, raw_csv_file):
        # Sorts the data by the YEAR and MONTH_STRING columns
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Assuming CSV columns are named 'MONTH_STRING' and 'YEAR'
        # Convert 'Year' column to strings to ensure correct sorting
        df['YEAR'] = df['YEAR'].astype(str)

        # Define the natural order of months
        month_order = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]

        # Convert 'Month' column to a categorical data type with custom sort order
        df['MONTH_STRING'] = pd.Categorical(df['MONTH_STRING'], categories=month_order, ordered=True)

        # Create a new column 'YearMonth' by concatenating 'Year' and 'Month'
        df['YearMonth'] = df['YEAR'] + df['MONTH_STRING'].astype(str)

        # Sort the DataFrame by 'Year' and 'Month'
        df.sort_values(by=['YEAR', 'MONTH'], inplace=True)

        # Drop the temporary 'YearMonth' column if you don't need it anymore
        df.drop('YearMonth', axis=1, inplace=True)

        # Save the sorted DataFrame back to a new CSV file
        new_file = raw_csv_file.replace('.csv', '_sorted.csv')
        df.to_csv(new_file, index=False)

        return new_file
        
    def add_location_row(self, raw_csv_file):
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Removes the 'WORCESTER POLYTECH text from the 'CUSTOMER_NM' column
        df['CUSTOMER_NM_Modified'] = df['CUSTOMER_NM'].str.replace('WORCESTER POLYTECH', '')

        # Combines the 'CUSTOMER_NM' and 'MONTH_STRING' columns into one column
        df['CUSTOMER_NM_Modified'] = df['CUSTOMER_NM_Modified']
        
        # Save the updated DataFrame to a new CSV file
        new_file = raw_csv_file.replace('.csv', '_location_row.csv')
        df.to_csv(new_file, index=False)

        return new_file
    
    def clean(self, raw_csv_file):
         # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Sets the columns I want to keep
        columns = [
            'YEAR',
            'TONNAGE',
            'MONTH_STRING',
            'CUSTOMER_NM_Modified'
        ]

        df = df[columns]
    
        # Save the updated DataFrame to a new CSV file
        new_file = raw_csv_file.replace('.csv', '_clean.csv')
        df.to_csv(new_file, index=False)

        return new_file
    
    def splitter(self, raw_csv_file):
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Separate the data into two DataFrames for each year
        df_2022 = df[df['YEAR'] == 2022]
        df_2023 = df[df['YEAR'] == 2023]

        # Save the DataFrames to new CSV files
        file_2022 = raw_csv_file.replace('.csv', '_2022.csv')
        file_2023 = raw_csv_file.replace('.csv', '_2023.csv')

        df_2022.to_csv(file_2022, index=False)
        df_2023.to_csv(file_2023, index=False)

        return file_2022, file_2023
    
    def process_data(self, raw_csv_file_2022, raw_csv_file_2023):
        # Read the input CSV files
        df_2022 = pd.read_csv(raw_csv_file_2022)
        df_2023 = pd.read_csv(raw_csv_file_2023)

        # Group by 'CUSTOMER_NM_Modified' and 'MONTH_STRING' and sum 'TONNAGE' for each DataFrame
        result_df1 = df_2022.groupby(['CUSTOMER_NM_Modified', 'MONTH_STRING'], as_index=False)['TONNAGE'].sum()
        result_df2 = df_2023.groupby(['CUSTOMER_NM_Modified', 'MONTH_STRING'], as_index=False)['TONNAGE'].sum()

        # Save the DataFrames to new CSV files
        file_2022 = raw_csv_file_2022.replace('.csv', '_processed.csv')
        file_2023 = raw_csv_file_2023.replace('.csv', '_processed.csv')

        result_df1.to_csv(file_2022, index=False)
        result_df2.to_csv(file_2023, index=False)

    def sorter_monthly(self, raw_csv_file_2022, raw_csv_file_2023):
        # Read the input CSV files
        df_2022 = pd.read_csv(raw_csv_file_2022)
        df_2023 = pd.read_csv(raw_csv_file_2023)

        # Assuming 'MONTH_STRING' is a categorical column with the order you want
        month_order = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]

        # Sort the DataFrames by 'MONTH_STRING' and 'CUSTOMER_NM_Modified'
        df_2022['MONTH_STRING'] = pd.Categorical(df_2022['MONTH_STRING'], categories=month_order, ordered=True)
        df_2022.sort_values(by=['MONTH_STRING', 'CUSTOMER_NM_Modified'], inplace=True)
        
        df_2023['MONTH_STRING'] = pd.Categorical(df_2023['MONTH_STRING'], categories=month_order, ordered=True)
        df_2023.sort_values(by=['MONTH_STRING', 'CUSTOMER_NM_Modified'], inplace=True)

        # Save the sorted DataFrames to new CSV files
        sorted_file_2022 = raw_csv_file_2022.replace('.csv', '_monthly.csv')
        sorted_file_2023 = raw_csv_file_2023.replace('.csv', '_monthly.csv')

        df_2022.to_csv(sorted_file_2022, index=False)
        df_2023.to_csv(sorted_file_2023, index=False)

        return sorted_file_2022, sorted_file_2023
    
    def monthly_total(self, raw_csv_file_2022, raw_csv_file_2023):
        # Read the input CSV files
        df_2022 = pd.read_csv(raw_csv_file_2022)
        df_2023 = pd.read_csv(raw_csv_file_2023)

        # Define a mapping from month names to month numbers
        month_to_num = {name: num for num, name in enumerate(month_name) if name}
        
        # Add a new column for month numbers, converting from month names
        df_2022['MONTH_NUM'] = df_2022['MONTH_STRING'].map(month_to_num)
        df_2023['MONTH_NUM'] = df_2023['MONTH_STRING'].map(month_to_num)
        
        # Group by 'MONTH_STRING' and sum 'TONNAGE' for each DataFrame
        result_df1 = df_2022.groupby(['MONTH_STRING', 'MONTH_NUM'], as_index=False)['TONNAGE'].sum()
        result_df2 = df_2023.groupby(['MONTH_STRING', 'MONTH_NUM'], as_index=False)['TONNAGE'].sum()
        
        # Sort the DataFrames based on the month number
        result_df1 = result_df1.sort_values('MONTH_NUM')
        result_df2 = result_df2.sort_values('MONTH_NUM')
        
        # Drop the 'MONTH_NUM' column as it is no longer needed after sorting
        result_df1 = result_df1.drop('MONTH_NUM', axis=1)
        result_df2 = result_df2.drop('MONTH_NUM', axis=1)

        # Save the DataFrames to new CSV files
        file_2022 = raw_csv_file_2022.replace('.csv', '_total.csv')
        file_2023 = raw_csv_file_2023.replace('.csv', '_total.csv')

        result_df1.to_csv(file_2022, index=False)
        result_df2.to_csv(file_2023, index=False)

        return file_2022, file_2023
    

if __name__ == "__main__":
    pass
