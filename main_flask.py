from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.models import Legend, FactorRange, ColumnDataSource, DataTable, TableColumn, LegendItem, Slider, Tabs, TabPanel
import math
import time
import pandas as pd
import helper as Helper
import numpy as np

class Main:
    def __init__(self):
        # Initialize the class variables
        # Creates a variable to hold the csv file name
        raw_csv_file = '22_23_WPI.csv'

        # Create an instance of the helper class as Helper, using Tools to call it
        # Also can brings in varialbles defined in the helper class
        self.Tools = Helper.MyClass()

        # Converts the list of numbers to a list of strings as Bokeh does not support integers
        raw_csv_file = self.Tools.convert_to_month_names(raw_csv_file)

        # Sorts the data by year and month
        raw_csv_file = self.Tools.sorter(raw_csv_file)

        # Call the add_location_row function from the helper class
        raw_csv_file = self.Tools.add_location_row(raw_csv_file)

        # Removes all the junk Columns
        raw_csv_file = self.Tools.clean(raw_csv_file)

        # Splits the data into two files, one for 2023 and one for 2022
        raw_csv_file = self.Tools.splitter(raw_csv_file)

        # Defines the two files for 2022 and 2023 to be used in the process_data function
        raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022.csv'
        raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023.csv'

        # Sums all the same locations pickups for a given location and month
        self.Tools.process_data(raw_csv_file_2022, raw_csv_file_2023)

        # Defines the two files for 2022 and 2023 sorter by month
        raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed.csv'
        raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed.csv'

        # Sorts the 2022 and 2023 data by month
        self.Tools.sorter_monthly(raw_csv_file_2022, raw_csv_file_2023)

        # Defines the two files for 2022 and 2023 that sums each per month
        raw_csv_file_2022 = '22_23_WPI_month_sorted_location_row_clean_2022_processed_monthly.csv'
        raw_csv_file_2023 = '22_23_WPI_month_sorted_location_row_clean_2023_processed_monthly.csv'

        self.Tools.monthly_total(raw_csv_file_2022, raw_csv_file_2023)

    def WPI_Waste(self):
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
        f1 = figure(
            title="22 WPI Recycling",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=x_range_2022,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
            
        )

        # Render glyph for 2022 year
        f1.vbar(
            x='Location_Date',
            top='TONNAGE',
            width=0.9,
            fill_alpha=0.5,
            fill_color='green',
            source = source_2022
        )

        # Add plot for 2023 year
        f2 = figure(
            title="23 WPI Recycling",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=x_range_2023,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
            
        )

        # Render glyph for 2023 year
        f2.vbar(
            x='Location_Date',
            top='TONNAGE',
            width=0.9,
            fill_alpha=0.5,
            fill_color='red',
            source = source_2023
        )

        # Rotate the x-axis labels
        f1.xaxis.major_label_orientation ="vertical"
        f2.xaxis.major_label_orientation ="vertical"

        # Combining plots 
        plots = row([f1,f2], sizing_mode="stretch_both")

        # Show results
        show(plots)

    def WPI_Waste_Monthly(self):
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
        f1 = figure(
            title="22 WPI Recycling Monthly",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=Month_2022,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
            
        )

        # Render glyph for 2022 year
        bar1 = f1.vbar(
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
        f1.add_layout(legend_2022, 'below')

        # Add plot for 2023 year
        f2 = figure(
            title="23 WPI Recycling Monthly",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=Month_2023,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
            
        )

        # Render glyph for 2023 year
        bar2 = f2.vbar(
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
        f2.add_layout(legend_2023, 'below')

        # Rotate the x-axis labels
        f1.xaxis.major_label_orientation ="vertical"
        f2.xaxis.major_label_orientation ="vertical"

        # Combining plots 
        plots = row([f1,f2], sizing_mode="stretch_both")

        # Show results
        show(plots)

    def WPI_Waste_Academic_Year(self):
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
        f = figure(
            title="WPI Recycling Academic Year",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=Month,
            y_range=(0, 100),
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
        )

        # Render glyphs for 2022 year
        bar1 = f.vbar(
            x=Month,
            top=Tons,
            fill_alpha=0.5,
            fill_color='blue',
        )

        # Add the polynomial trend line glyph to the plot
        f.line(
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
        f.add_layout(legend, 'below')

        # Rotate the x-axis labels
        f.xaxis.major_label_orientation = "vertical"
  
        # Show the result
        show(f)

    def Robot_Recycling(self):
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

        # Variables for the caluclation
        robot_rate = 960 # Items per day
        item_wieght = 0.5 # Pounds
        number_of_items = df_combined['TONNAGE'].sum() * 2000 / item_wieght
        recycling_rate = 0.19 # 19% of items that can actually be recycled
        true_number_of_items = number_of_items * recycling_rate
        print(true_number_of_items)

        # Add plot for both years on the same graph
        f1 = figure(
            title="WPI Recycling Academic Year",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=Month,
            y_range=(0, 100),
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
        )

        bar1 = f1.circle(
            x=Month,
            y=Tons,
            fill_alpha=0.5,
            fill_color='blue',
        )

        # Add the polynomial trend line glyph to the plot
        f1.line(
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
        f1.add_layout(legend, 'below')

        # Rotate the x-axis labels
        f1.xaxis.major_label_orientation = "vertical"
  
        # Show the result
        show(f1)

    def profitability(self):
        pass

    def roi(self):
        pass 

if __name__ == "__main__":
    # Run init
    Main().__init__

    # Graph the yearly charts
    Main().WPI_Waste()

    time.sleep(0.5)

    # Graph the monthly charts
    Main().WPI_Waste_Monthly()

    time.sleep(0.5)

    # Graph the academic year
    Main().WPI_Waste_Academic_Year()

    time.sleep(0.5)

    # Graph the robot recycling
    #Main().Robot_Recycling()



# Example function to create models
def create_models():
    # Your code to create new models goes here
    # For example, creating new Tabs
    Locations_Panel = TabPanel(child=plots_Locations, title="WPI Recycling Locations") 
    Monthly_panel = TabPanel(child=plots_monthly, title="22 WPI Recycling Monthly")
    Academic_Year_panel = TabPanel(child=academic_year, title="WPI Recycling Academic Year")
    Robot_panel = TabPanel(child=Robot_Rate_Layout, title="Robot Calculation")

    tabs = Tabs(tabs=[Locations_Panel, Monthly_panel, Academic_Year_panel, Robot_panel])
    return tabs

# Updated modify_doc function
def modify_doc(doc):
    tabs = create_models()
    doc.add_root(tabs)
