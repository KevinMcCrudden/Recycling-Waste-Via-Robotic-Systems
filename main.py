from bokeh.plotting import figure, show
from bokeh.layouts import column, row
import pandas

# Read in CSV
df = pandas.read_csv('22-23_WM_Recycling_Data.csv')

# Assings the value of the column 'MONTH' to the variable 'Month'
# Also converts the list of numbers to a list of strings as Bokeh does not support integers

def convert_to_month_names(month_list):
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

# Convert the month numbers to month names
Month = convert_to_month_names(df['MONTH'])
print(Month)

# Assings the value of the column 'TONNAGE' to the variable 'Tons'
Tons = df['TONNAGE']

# Add plot for orange cars
p = figure(
    y_range=Month,
    title="22-23 WPI Recycling Data",
    x_axis_label="Weight in Tons",
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph for orange cars
p.hbar(
    y=Tons,
    right=Month,
    left=0,
    height=0.4,
    color="orange",
    fill_alpha=0.5
)

# Show results
show(p)