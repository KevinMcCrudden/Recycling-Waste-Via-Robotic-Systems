from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.models import Legend, FactorRange, ColumnDataSource, DataTable, TableColumn, LegendItem, Slider, Tabs, TabPanel
import pandas as pd
import helper as Helper
import numpy as np

# Initialize the class variables
# Creates a variable to hold the csv file name
raw_csv_file = '22_23_WPI.csv'

# Create an instance of the helper class as Helper, using Tools to call it
# Also can brings in varialbles defined in the helper class
Tools = Helper.MyClass()

# Converts the list of numbers to a list of strings as Bokeh does not support integers
raw_csv_file = Tools.convert_to_month_names(raw_csv_file)

# Sorts the data by year and month
raw_csv_file = Tools.sorter(raw_csv_file)

# Call the add_location_row function from the helper class
raw_csv_file = Tools.add_location_row(raw_csv_file)

# Removes all the junk Columns
raw_csv_file = Tools.clean(raw_csv_file)

# Splits the data into two files, one for 2023 and one for 2022
raw_csv_file = Tools.splitter(raw_csv_file)

# Defines the two files for 2022 and 2023 to be used in the process_data function
raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022.csv'
raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023.csv'

# Sums all the same locations pickups for a given location and month
Tools.process_data(raw_csv_file_2022, raw_csv_file_2023)

# Defines the two files for 2022 and 2023 sorter by month
raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed.csv'
raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed.csv'

# Sorts the 2022 and 2023 data by month
Tools.sorter_monthly(raw_csv_file_2022, raw_csv_file_2023)

# Defines the two files for 2022 and 2023 that sums each per month
raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly.csv'
raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly.csv'

Tools.monthly_total(raw_csv_file_2022, raw_csv_file_2023)

# Set the CSV file for the 2022 year and 2023
output_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly.csv'
output_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly.csv'

# WPI Location Totals
########################################################################################
# Read the CSV file that was created by the helper class from 2022 and 2023
df_2022 = pd.read_csv(output_csv_file_2022)
df_2023 = pd.read_csv(output_csv_file_2023)

# Concatenate 'CUSTOMER_NM_Modified' and 'MONTH_STRING' columns to create a new column
df_2022['Location_Date'] = df_2022['CUSTOMER_NM_Modified'] + ' ' + df_2022['MONTH_STRING']
df_2023['Location_Date'] = df_2023['CUSTOMER_NM_Modified'] + ' ' + df_2023['MONTH_STRING']

# Combine Location and Month into a single FactorRange for x-axis
x_range_2022 = FactorRange(*df_2022['Location_Date'].unique())
x_range_2023 = FactorRange(*df_2023['Location_Date'].unique())

# Create a ColumnDataSource for the data from 2022
source_2022 = ColumnDataSource(df_2022)
source_2023 = ColumnDataSource(df_2023)

# Add plot for 2022 year
Locations_2022 = figure(
    title="22 WPI Recycling",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=x_range_2022,
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    
)

# Render glyph for 2022 year
Locations_2022.vbar(
    x='Location_Date',
    top='TONNAGE',
    width=0.9,
    fill_alpha=0.5,
    fill_color='green',
    source = source_2022
)

# Add plot for 2023 year
Locations_2023 = figure(
    title="23 WPI Recycling",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=x_range_2023,
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    
)

# Render glyph for 2023 year
Locations_2023.vbar(
    x='Location_Date',
    top='TONNAGE',
    width=0.9,
    fill_alpha=0.5,
    fill_color='red',
    source = source_2023
)

# Rotate the x-axis labels
Locations_2022.xaxis.major_label_orientation ="vertical"
Locations_2023.xaxis.major_label_orientation ="vertical"

# Combining plots 
plots_Locations = row([Locations_2022,Locations_2023], sizing_mode='scale_both')

# Monthly Totals
########################################################################################
# Set the CSV file for the montly totals
monthly_totals_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly_total.csv'
monthly_totals_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly_total.csv'

# Read the CSV file that was created by the helper class from 2022 and 2023
df_2022 = pd.read_csv(monthly_totals_2022)
df_2023 = pd.read_csv(monthly_totals_2023)

# Assings the value of the column 'TONNAGE' to the variable Tons for 2022 and 2023
Tons_2022 = df_2022['TONNAGE']
Tons_2023 = df_2023['TONNAGE']

# Assings the value of the column 'MONTH_STRING' to the variable Month for 2022 and 2023
Month_2022 = df_2022['MONTH_STRING']
Month_2023 = df_2023['MONTH_STRING']

# Add plot for 2022 year
Monthly_2022 = figure(
    title="22 WPI Recycling Monthly",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Month_2022,
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    
)

# Render glyph for 2022 year
bar1 = Monthly_2022.vbar(
    x=Month_2022,
    top=Tons_2022,
    fill_alpha=0.5,
    fill_color='red',
)

# Add a legend for 2022
legend_2022 = Legend(
    items=[(f"{df_2022['TONNAGE'].sum()} Tons", [bar1])],
    location="center",
    orientation="horizontal",
    click_policy="hide"
)

# Add the legend to the plot
Monthly_2022.add_layout(legend_2022, 'below')

# Add plot for 2023 year
Monthly_2023 = figure(
    title="23 WPI Recycling Monthly",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Month_2023,
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    
)

# Render glyph for 2023 year
bar2 = Monthly_2023.vbar(
    x=Month_2023,
    top=Tons_2023,
    fill_alpha=0.5,
    fill_color='red',
)

legend_2023 = Legend(
    items=[(f"{df_2023['TONNAGE'].sum()} Tons", [bar2])],
    location="center",
    orientation="horizontal",
    click_policy="hide"
)

# Add the legend to the plot
Monthly_2023.add_layout(legend_2023, 'below')

# Rotate the x-axis labels
Monthly_2022.xaxis.major_label_orientation ="vertical"
Monthly_2023.xaxis.major_label_orientation ="vertical"

# Combining plots 
plots_monthly = row([Monthly_2022,Monthly_2023], sizing_mode='scale_both')

# Academic Year Total with polynomial trend line
########################################################################################
# Set the CSV file for the montly totals
monthly_totals_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly_total.csv'
monthly_totals_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly_total.csv'

# Read the CSV file that was created by the helper class from 2022 and 2023
df_2022 = pd.read_csv(monthly_totals_2022)
df_2023 = pd.read_csv(monthly_totals_2023)

# Concetenate the two years together
df_combined = pd.concat([df_2022, df_2023])

# Assings the value of the column 'TONNAGE' to the variable 'Tons'
Tons = df_combined['TONNAGE']

# Assings the value of the column 'Month' to the variable 'Month'
Month = df_combined['MONTH_STRING']

# Fit a polynomial to the data
degree = 3 # Set the degree of the polynomial
coefficients = np.polyfit(range(len(Tons)), Tons, degree)
polynomial = np.poly1d(coefficients)

# Format the polynomial equation as a string
equation_parts = []
for deg, coef in enumerate(coefficients[::-1]):
    if deg == 0:
        part = f"{coef:.2f}"
    elif deg == 1:
        part = f"{coef:+.2f}x"
    else:
        part = f"{coef:+.2f}x^{deg}"
    equation_parts.append(part)
equation = "y = " + " ".join(equation_parts)

# Generate x values for the trend line
x_values = np.linspace(0, len(Tons), 100)

# Calculate corresponding y values for the trend line
y_values = polynomial(x_values)

# Add plot for both years on the same graph
academic_year = figure(
    title="WPI Recycling Academic Year",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Month,
    y_range=(0, 100),
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
    sizing_mode='scale_both'
)

# Render glyphs for 2022 year
bar1 = academic_year.vbar(
    x=Month,
    top=Tons,
    fill_alpha=0.5,
    fill_color='blue',
)

# Add the polynomial trend line glyph to the plot
academic_year.line(
    x_values, 
    y_values, 
    line_color='red', 
    line_width=2, 
    legend_label=f'Polynomial Trend Line: {equation}'
)

# Add a legend for 2022
legend = Legend(
    items=[(f"{df_combined['TONNAGE'].sum()} Tons", [bar1])],
    location="center",
    orientation="horizontal",
    click_policy="hide"
)

# Add the legend to the plot
academic_year.add_layout(legend, 'below')

# Rotate the x-axis labels
academic_year.xaxis.major_label_orientation = "vertical"

# Robot Calculation
########################################################################################
# Set the CSV file for the montly totals
monthly_totals_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly_total.csv'
monthly_totals_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly_total.csv'

# Read the CSV file that was created by the helper class from 2022 and 2023
df_2022 = pd.read_csv(monthly_totals_2022)
df_2023 = pd.read_csv(monthly_totals_2023)

# Concetenate the two years together
df_combined = pd.concat([df_2022, df_2023])

# Assings the value of the column 'TONNAGE' to the variable Tons
Tons = df_combined['TONNAGE']

# Assings the value of the column 'MONTH_STRING' to the variable Month
Month = df_combined['MONTH_STRING']

# Fit a polynomial to the data
degree = 3  # Set the degree of the polynomial
coefficients = np.polyfit(range(len(Tons)), Tons, degree)
polynomial = np.poly1d(coefficients)

# Format the polynomial equation as a string
equation_parts = []
for deg, coef in enumerate(coefficients[::-1]):
    if deg == 0:
        part = f"{coef:.2f}"
    elif deg == 1:
        part = f"{coef:+.2f}x"
    else:
        part = f"{coef:+.2f}x^{deg}"
    equation_parts.append(part)
equation = "y = " + " ".join(equation_parts)

# Generate x values for the trend line
x_values = np.linspace(0, len(Tons), 100)

# Calculate corresponding y values for the trend line
y_values = polynomial(x_values)

# Define initial data source for the polynomial trend line
source = ColumnDataSource(data={'x': x_values, 'y': y_values})

# Variables for the caluclation
robot_rate = 960 # Items per day
item_wieght = 0.5 # Pounds
number_of_items = df_combined['TONNAGE'].sum() * 2000 / item_wieght
recycling_rate = 0.19 # 19% of items that can actually be recycled
true_number_of_items = number_of_items * recycling_rate

# Add plot for both years on the same graph
Robot_rate = figure(
    title="WPI Recycling Academic Year",
    x_axis_label="Months of the year",
    y_axis_label="Weight in Tons",
    x_range=Month,
    y_range=(0, 100),
    tools="pan,box_select,zoom_in,zoom_out,save,reset",
)

bar1 = Robot_rate.circle(
    x=Month,
    y=Tons,
    fill_alpha=0.5,
    fill_color='blue',
)

# Add the polynomial trend line glyph to the plot
Robot_rate.line(
    x = 'x', 
    y = 'y',
    source = source, 
    line_color='red', 
    line_width=2, 
    legend_label=f'Polynomial Trend Line: {equation}'
)

# Add a legend for 2022
legend = Legend(
    items=[(f"{df_combined['TONNAGE'].sum()} Tons", [bar1])],
    location="center",
    orientation="horizontal",
    click_policy="hide"
)

# Add the legend to the plot
Robot_rate.add_layout(legend, 'below')

# Rotate the x-axis labels
Robot_rate.xaxis.major_label_orientation = "vertical"

# Slider stuff
degree_slider = Slider(
    start=1, 
    end=10, 
    value=3, 
    step=1, 
    title="Degree of Polynomial"
)

# Callback function for the slider
def update_polynomial(attr, old, new):
    # Calculate new polynomial coefficients and y-values
    new_degree = degree_slider.value
    new_coefficients = np.polyfit(range(len(Tons)), Tons, new_degree)
    new_polynomial = np.poly1d(new_coefficients)
    new_y_values = new_polynomial(x_values)

    # Update the data source with new y-values
    source.data = {'x': x_values, 'y': new_y_values}

    # Optionally, update the legend label (if necessary)
    Robot_rate.legend.items[0] = LegendItem(label=f'Polynomial Trend: Degree {new_degree}', renderers=[Robot_rate.renderers[1]])

# Attach the callback to the slider
degree_slider.on_change('value', update_polynomial)

# Created layout for slider and the plot
Robot_Rate_Layout = column(degree_slider, Robot_rate)

# Adjusts the size of the plot and slider
Robot_Rate_Layout.sizing_mode = "scale_both"


# Shows all plots
########################################################################################
Locations_Panel = TabPanel(child=plots_Locations, title="WPI Recycling Locations")
Monthly_panel = TabPanel(child=plots_monthly, title="22 WPI Recycling Monthly")
Academic_Year_panel = TabPanel(child=academic_year, title="WPI Recycling Academic Year")
Robot_panel = TabPanel(child=Robot_Rate_Layout, title="Robot Calculation")

tabs = Tabs(tabs=[Locations_Panel, Monthly_panel, Academic_Year_panel, Robot_panel])

# Brings up the tabs for bokeh server
curdoc().add_root(tabs)