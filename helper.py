import pandas as pd

class MyClass:
    def __init__(self):
        # Initialize the class with the CSV file
        pass

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
        new_file = raw_csv_file.replace('.csv', '_converted_month_names.csv')
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
            
    def monthly_totals(self, raw_csv_file):
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Removes the 'WORCESTER POLYTECH text from the 'CUSTOMER_NM' column
        df['CUSTOMER_NM_Modified'] = df['CUSTOMER_NM'].str.replace('WORCESTER POLYTECH', '')

        # Combines the 'CUSTOMER_NM' and 'MONTH_STRING' columns into one column
        df['CUSTOMER_NM_Modified+MONTH_STRING'] = df['CUSTOMER_NM_Modified'] + ' - ' + df['MONTH_STRING'].astype(str) + ' - ' + df['YEAR'].astype(str)

        # Save the updated DataFrame to a new CSV file
        new_file = raw_csv_file.replace('.csv', '_monthly_totals.csv')
        df.to_csv(new_file, index=False)
        return new_file

    def remove_duplicates_sum(self, raw_csv_file):
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Combine columns to create a new column for grouping
        df['Combined_Column'] = df['CUSTOMER_NM_Modified+MONTH_STRING']

        # Group by the combined column and sum the TONNAGE
        grouped_df = df.groupby(['Combined_Column'])['TONNAGE'].sum().reset_index()

        # Save the result to a new CSV file
        new_file = raw_csv_file.replace('.csv', '_duplicates_sum.csv')
        grouped_df.to_csv(new_file, index=False)
        return new_file
    
    def create_yearly_files(self, raw_csv_file):
        # Read the input CSV file
        df = pd.read_csv(raw_csv_file)

        # Extract the year from the 'Combined_Column' and convert it to integer
        df['Year'] = df['Combined_Column'].str.extract(r'(\d{4})').astype(int)

        # Split the DataFrame into two based on the 'Year' column
        df_2022 = df[df['Year'] == 2022]
        df_2023 = df[df['Year'] == 2023]

        # Save the results to two new CSV files
        file_2022 = raw_csv_file.replace('.csv', '_2022.csv')
        file_2023 = raw_csv_file.replace('.csv', '_2023.csv')

        df_2022.to_csv(file_2022, index=False)
        df_2023.to_csv(file_2023, index=False)

        return file_2022, file_2023

if __name__ == "__main__":
    pass
