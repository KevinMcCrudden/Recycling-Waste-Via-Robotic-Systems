import pandas as pd

class MyClass:
    def __init__(self):
        # Initialize the class with the CSV file
        pass

    def convert_to_month_names(self, csv_file):
        # Define a dictionary to map integers to month names
        # Read the input CSV file
        df = pd.read_csv(csv_file)

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
        df.to_csv(csv_file, index=False)
    
    def sorter(self, csv_file):
        # Sorts the data by the YEAR and MONTH_STRING columns
        # Read the input CSV file
        df = pd.read_csv(csv_file)

        # Converts 'YEAR' and 'MONTH' columns to strings to ensure correct sorting
        df['YEAR'] = df['YEAR'].astype(str)
        df['MONTH_STRING'] = df['MONTH_STRING'].astype(str)

        # Create a new column 'YearMonth' by concatenating 'Year' and 'Month'
        df['YearMonth'] = df['YEAR'] + df['MONTH_STRING']

        # Sort the DataFrame by 'YearMonth'
        df.sort_values(by='YearMonth', inplace=True)

        # Drop the temporary 'YearMonth' column if you don't need it anymore
        df.drop('YearMonth', axis=1, inplace=True)

        # Save the sorted DataFrame back to a CSV file
        df.to_csv(csv_file, index=False)
            
    def monthly_totals(self, csv):
        pass

if __name__ == "__main__":
    pass