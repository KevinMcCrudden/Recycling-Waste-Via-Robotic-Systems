from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.models import Legend, FactorRange, ColumnDataSource, DataTable, TableColumn, LegendItem, Slider, Tabs, TabPanel, Div, DatetimeTickFormatter
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

# Combines the two files for 2022 and 2023
raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly_total.csv'
raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly_total.csv'

Tools.combine(raw_csv_file_2022, raw_csv_file_2023)

def Locations():
    # Set the CSV file for the 2022 year and 2023
    output_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly.csv'
    output_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly.csv'

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
    Locations_Plot_2022 = figure(
        title="22 WPI Recycling",
        x_axis_label="Months of the year",
        y_axis_label="Weight in Tons",
        x_range=x_range_2022,
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
        
    )

    # Render glyph for 2022 year
    Locations_Plot_2022.vbar(
        x='Location_Date',
        top='TONNAGE',
        width=0.9,
        fill_alpha=0.5,
        fill_color='green',
        source = source_2022
    )

    # Add plot for 2023 year
    Locations_Plot_2023 = figure(
        title="23 WPI Recycling",
        x_axis_label="Months of the year",
        y_axis_label="Weight in Tons",
        x_range=x_range_2023,
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
        
    )

    # Render glyph for 2023 year
    Locations_Plot_2023.vbar(
        x='Location_Date',
        top='TONNAGE',
        width=0.9,
        fill_alpha=0.5,
        fill_color='red',
        source = source_2023
    )

    # Rotate the x-axis labels
    Locations_Plot_2022.xaxis.major_label_orientation ="vertical"
    Locations_Plot_2023.xaxis.major_label_orientation ="vertical"

    # Combining plots 
    plots = row([Locations_Plot_2022,Locations_Plot_2023])

    # Adjusts the size of the plot
    plots.sizing_mode = "scale_both"

    # Show results
    return plots

def Months():
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
    Months_Plot_2022 = figure(
        title="22 WPI Recycling Monthly",
        x_axis_label="Months of the year",
        y_axis_label="Weight in Tons",
        x_range=Month_2022,
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
        
    )

    # Render glyph for 2022 year
    bar1 = Months_Plot_2022.vbar(
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
    Months_Plot_2022.add_layout(legend_2022, 'below')

    # Add plot for 2023 year
    Months_Plot_2023 = figure(
        title="23 WPI Recycling Monthly",
        x_axis_label="Months of the year",
        y_axis_label="Weight in Tons",
        x_range=Month_2023,
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
        
    )

    # Render glyph for 2023 year
    bar2 = Months_Plot_2023.vbar(
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
    Months_Plot_2023.add_layout(legend_2023, 'below')

    # Rotate the x-axis labels
    Months_Plot_2022.xaxis.major_label_orientation ="vertical"
    Months_Plot_2023.xaxis.major_label_orientation ="vertical"

    # Combining plots 
    plots = row([Months_Plot_2022,Months_Plot_2023])

    # Adjusts the size of the plot
    plots.sizing_mode = "scale_both"

    # Show results
    return plots

def Academic_Year():
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

    # Generate x values for the trend line
    x_values = np.linspace(0, len(Tons), 100)

    # Calculate corresponding y values for the trend line
    y_values = polynomial(x_values)

    # Define initial data source for the polynomial trend line
    source_polynomial = ColumnDataSource(data={'x': x_values, 'y': y_values})

    # Add plot for both years on the same graph
    Academic_Year_Plot = figure(
        title="WPI Recycling Academic Year",
        x_axis_label="Months of the year",
        y_axis_label="Weight in Tons",
        x_range=Month,
        y_range=(0, 100),
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
    )

    # Render glyphs for academic year
    bar1 = Academic_Year_Plot.vbar(
        x=Month,
        top=Tons,
        fill_alpha=0.5,
        fill_color='blue',
    )

    # Add the polynomial trend line glyph to the plot
    glyph1 = Academic_Year_Plot.line(
        x = 'x', 
        y = 'y',
        source = source_polynomial, 
        line_color='green', 
        line_width=2,
    )

    # Add a legend for the total at the bottom
    legend = Legend(
        items=[(f"{df_combined['TONNAGE'].sum()} Tons", [bar1])],
        location="center",
        orientation="horizontal",
        click_policy="hide"
    )

     # Add the legend to the plot
    Academic_Year_Plot.add_layout(legend, 'below')

    # Define a slider for the degree of the polynomial
    degree_slider = Slider(
        start=1, 
        end=10, 
        value=3, 
        step=1, 
        title="Degree of Polynomial"
    )

    # Initial polynomial equation for display
    equation_parts = [f"{coeff:.2f}x^{i}" if i > 0 else f"{coeff:.2f}" for i, coeff in enumerate(coefficients[::-1])]
    equation = "y = " + " + ".join(equation_parts)

    # Define a Div for the polynomial equation
    equation_div = Div(text=f"Polynomial Trend Line: {equation}", width=400, height=30)

    def update_polynomial(attr, old, new):
        # Recalculate polynomial and update plot based on slider
        new_degree = degree_slider.value
        new_coefficients = np.polyfit(range(len(Tons)), Tons, new_degree)
        new_polynomial = np.poly1d(new_coefficients)
        new_y_values = new_polynomial(x_values)
        
        # Update source data for the line
        source_polynomial.data.update({'x': x_values, 'y': new_y_values})
        
        # Update the polynomial equation display
        new_equation_parts = [f"{coeff:.2f}x^{i}" if i > 0 else f"{coeff:.2f}" for i, coeff in enumerate(new_coefficients[::-1])]
        new_equation = "y = " + " + ".join(new_equation_parts)
        equation_div.text = f"Polynomial Trend Line: {new_equation}"

    # Attach the callback to the slider
    degree_slider.on_change('value', update_polynomial)

    ## Graph adjustments
    # Rotate the x-axis labels
    Academic_Year_Plot.xaxis.major_label_orientation = "vertical"

    # Combine the plot and slider into a layout
    Academic_Year_Layout = column([Academic_Year_Plot, degree_slider, equation_div])

    # Adjusts the size of the plot
    Academic_Year_Layout.sizing_mode = "scale_both"

    # Show the result
    return Academic_Year_Layout

def Robot_Rate():
    # Variables for the caluclation
    robot_rate = 40 # Items per hour
    hours_per_day = 24 # Hours
    item_weight = 0.5 # Individual item weight in pounds
    recycling_rate = 0.19 # 19% of items that can actually be recycled
    robot_uptime = 0.90 # 90% uptime
    
    # Set the CSV file for the montly totals
    combined = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly_total_combined.csv'

    # Read the CSV file that was created by the helper class from 2022 and 2023
    df = pd.read_csv(combined)

    # Assings the value of the column 'TONNAGE' to the variable Tons
    Tons = df['TONNAGE']

    # Assings the value of the column 'MONTH_STRING' to the variable Month
    Month = df['MONTH_STRING']

    # Assigns the value of the column 'DAYS_IN_MONTH' to Days
    Days = df['DAYS_IN_MONTH']

    # Creates plot for the robot rate
    Robot_Rate_Plot = figure(
        title="Robot Rate",
        x_axis_label="Months of the year",
        y_axis_label="Weight in Tons",
        x_range=Month,
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
    )

    # Render glyph for the amount of recycling for each month
    bar1 = Robot_Rate_Plot.vbar(
        x=Month,
        top=Tons,
        fill_alpha=0.5,
        fill_color='red',
    )

    # Adjusts the size of the plot and slider
    Robot_Rate_Plot.sizing_mode = "scale_both"

    # Rotate the x-axis labels
    Robot_Rate_Plot.xaxis.major_label_orientation = "vertical"

    # Show the result
    return Robot_Rate_Plot

def profitability():

    pass

def roi():
    pass 

# Your code to create new models goes here
# For example, creating new Tabs
Locations_panel = TabPanel(child=Locations(), title="WPI Recycling Locations") 
Monthly_panel = TabPanel(child=Months(), title="WPI Recycling Monthly")
Academic_Year_panel = TabPanel(child=Academic_Year(), title="WPI Recycling Academic Year")
Robot_Rate_panel = TabPanel(child=Robot_Rate(), title="Robot Rate")

tabs = Tabs(tabs=[Locations_panel, Monthly_panel, Academic_Year_panel, Robot_Rate_panel])

# Add the layout to the current document
curdoc().add_root(tabs)