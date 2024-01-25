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

# This splits the 2022 and 2023 years apart to graph them separately
raw_csv_file = Tools.create_yearly_files(raw_csv_file)

# Set the CSV file for the 2022 year
output_csv_file_2022 = '22-23_WM_Recycling_Data_converted_month_names_sorted_monthly_totals_duplicates_sum_2022.csv'

# Set the CSV file for the 2023 year
output_csv_file_2023 = '22-23_WM_Recycling_Data_converted_month_names_sorted_monthly_totals_duplicates_sum_2023.csv'

# Read the CSV file that was created by the helper class from 2022
df_2022 = pd.read_csv(output_csv_file_2022)

# Read the CSV file that was created by the helper class from 2023
df_2023 = pd.read_csv(output_csv_file_2023)

# Assings the value of the column 'TONNAGE' to the variable 'Tons' for 2022
Tons_2022 = df_2022['TONNAGE']

# Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year' for 2022
Location_Date_Year_2022 = df_2022['Combined_Column']

# Assings the value of the column 'TONNAGE' to the variable 'Tons' for 2022
Tons_2023 = df_2023['TONNAGE']

# Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year' for 2022
Location_Date_Year_2023 = df_2023['Combined_Column']

# Add plot for 2022 year
f1 = figure(
    title="22 WPI Recycling Data",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Location_Date_Year_2022,
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    sizing_mode="stretch_both",
    
)

# Render glyph for 2022 year
f1.vbar(
    x=Location_Date_Year_2022,
    top=Tons_2022,
    fill_alpha=0.5,
    line_color='green',
)

# Add plot for 2023 year
f2 = figure(
    title="23 WPI Recycling Data",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Location_Date_Year_2023,
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    sizing_mode="stretch_both",
    
)

# Render glyph for 2023 year
f2.vbar(
    x=Location_Date_Year_2023,
    top=Tons_2023,
    fill_alpha=0.5,
    line_color='green',
)


# Rotate the x-axis labels
f1.xaxis.major_label_orientation ="vertical"
f2.xaxis.major_label_orientation ="vertical"

# Combining plots 
plots = row([f1,f2], sizing_mode="stretch_both")

# Show results
show(plots)