from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
import pandas as pd
import helper as Helper

# Creates a variable to hold the csv file name
csv_file = 'Testing.csv'

# Create an instance of the helper class as Helper, using Tools to call it
Tools = Helper.MyClass()

# Assings the value of the column 'MONTH' to the variable 'Month'
# Also converts the list of numbers to a list of strings as Bokeh does not support integers
Tools.convert_to_month_names(csv_file)

# Sorts the data by year and month
Tools.sorter(csv_file)

# Combines the 'CUSTOMER_NM' column with the 'MONTH_STRING' column
Tools.monthly_totals(csv_file)

# Removes duplicate locations during the same month and totals the TONNAGE
Tools.remove_duplicates_sum(csv_file)

# Read the CSV file
df = pd.read_csv(csv_file)

# Assings the value of the column 'TONNAGE' to the variable 'Tons'
#Tons = df['TONNAGE']

# Assings the value of the column 'CUSTOMER_NM+MONTH_STRING' to the variable 'Location_Date'
#Location_Date = df['CUSTOMER_NM+MONTH_STRING']

# # Add plot for orange cars
# p = figure(
#     title="22-23 WPI Recycling Data",
#     x_axis_label="Months of the year",
#     y_axis_label="Weight in Tons",
#     x_range=Location_Date,
#     tools="pan,box_select,zoom_in,zoom_out,save,reset"
# )

# # Render glyph for orange cars
# p.vbar(
#     x=Location_Date,
#     top=Tons,
#     width=0.9,
#     fill_alpha=0.5,
#     line_color='green',
# )

# # Show results
# show(p)