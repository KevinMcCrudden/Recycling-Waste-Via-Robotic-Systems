from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
import pandas as pd
import helper as Helper

# Creates a variable to hold the csv file name
raw_csv_file = '22-23_WM_Recycling_Data.csv'

# Create an instance of the helper class as Helper, using Tools to call it
Tools = Helper.MyClass()

# Assings the value of the column 'MONTH' to the variable 'Month'
# Also converts the list of numbers to a list of strings as Bokeh does not support integers
raw_csv_file = Tools.convert_to_month_names(raw_csv_file)

# Sorts the data by year and month
raw_csv_file = Tools.sorter(raw_csv_file)

# Combines the 'CUSTOMER_NM' column with the 'MONTH_STRING' column
raw_csv_file = Tools.monthly_totals(raw_csv_file)

# Removes duplicate locations during the same month and totals the TONNAGE
raw_csv_file = Tools.remove_duplicates_sum(raw_csv_file)

# # Set the CSV file that was created by the helper class as a variable
# output_csv_file = 'whatever_this_is.csv'

# # Read the CSV file that was created by the helper class
# df = pd.read_csv(output_csv_file)

# # Assings the value of the column 'TONNAGE' to the variable 'Tons'
# Tons = df['TONNAGE']

# # Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year'
# Location_Date_Year = df['Combined_Column']

# # Add plot for orange cars
# p = figure(
#     title="22-23 WPI Recycling Data",
#     x_axis_label="Months of the year",
#     y_axis_label="Weight in Tons",
#     x_range=Location_Date_Year,
#     tools="pan,box_select,zoom_in,zoom_out,save,reset"
# )

# # Render glyph for orange cars
# p.vbar(
#     x=Location_Date_Year,
#     top=Tons,
#     width=0.9,
#     fill_alpha=0.5,
#     line_color='green',
# )

# # Show results
# show(p)