from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
import pandas
import helper as Helper

# Read the CSV file
df = pandas.read_csv('22-23_WM_Recycling_Data.csv')

# Assuming your CSV columns are named 'MONTH' and 'YEAR'
# Convert 'YEAR' and 'MONTH' columns to strings to ensure correct sorting
df['YEAR'] = df['YEAR'].astype(str)
df['MONTH'] = df['MONTH'].astype(str)

# Create a new column 'YearMonth' by concatenating 'Year' and 'Month'
df['YearMonth'] = df['YEAR'] + df['MONTH']

# Sort the DataFrame by 'YearMonth'
df.sort_values(by='YearMonth', inplace=True)

# Drop the temporary 'YearMonth' column if you don't need it anymore
df.drop('YearMonth', axis=1, inplace=True)

# Save the sorted DataFrame back to a CSV file
df.to_csv('test.csv', index=False)

# Create an instance of the helper class as Helper, using Tools to call it
Tools = Helper.MyClass()

# Assings the value of the column 'MONTH' to the variable 'Month'
# Also converts the list of numbers to a list of strings as Bokeh does not support integers
Month = Tools.convert_to_month_names(df['MONTH'])

# Assings the value of the column 'TONNAGE' to the variable 'Tons'
Tons = df['TONNAGE']

# Add plot for orange cars
p = figure(
    title="22-23 WPI Recycling Data",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Month,
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph for orange cars
p.vbar(
    x=Month,
    top=Tons,
    width=0.9,
    fill_alpha=0.5,
    line_color='green',
)

# Show results
show(p)