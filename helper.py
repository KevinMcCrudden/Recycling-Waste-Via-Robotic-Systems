class MyClass:
    def __init__(self):
        # Constructor (initialize your class attributes here)
        pass

    def convert_to_month_names(self, month_list):
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

        # Convert each integer to its corresponding month name
        month_names = [month_mapping.get(month, 'Invalid Month') for month in month_list]

        return month_names
    
    def sorter(self, month_list):
        pass

if __name__ == "__main__":
    pass