from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.models import Legend, ColumnDataSource, DataTable, TableColumn, LegendItem
import math
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
    
    def WPI_Waste(self):
        # Set the CSV file for the 2022 year
        output_csv_file_2022 = '22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2022.csv'

        # Set the CSV file for the 2023 year
        output_csv_file_2023 = '22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2023.csv'

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
            title="22 WPI Recycling",
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
            fill_color='green',
        )

        # Add plot for 2023 year
        f2 = figure(
            title="23 WPI Recycling",
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
            fill_color='green',
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
        monthly_totals_2022 = '22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2022.csv'
        monthly_totals_2023 = '22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2023.csv'
        
        # Call the monthly_total function from the helper class
        self.Tools.monthly_total(monthly_totals_2022, monthly_totals_2023)

        # Read the CSV file that was created by the helper class from 2022
        df_2022 = pd.read_csv('22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2022_monthly_totals.csv')

        # Read the CSV file that was created by the helper class from 2023
        df_2023 = pd.read_csv('22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2023_monthly_totals.csv')

        # Assings the value of the column 'TONNAGE' to the variable 'Tons' for 2022
        Tons_2022 = df_2022['TONNAGE']

        # Assings the value of the column 'Month' to the variable 'Month' for 2022
        Month_2022 = df_2022['Month']

        # Assings the value of the column 'TONNAGE' to the variable 'Tons' for 2022
        Tons_2023 = df_2023['TONNAGE']

        # Assings the value of the column 'Month' to the variable 'Month' for 2022
        Month_2023 = df_2023['Month']

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
        monthly_totals_2022 = '22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2022.csv'
        monthly_totals_2023 = '22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2023.csv'
        
        # Call the monthly_total function from the helper class
        self.Tools.monthly_total(monthly_totals_2022, monthly_totals_2023)

        # Read the CSV file that was created by the helper class from 2022
        df_2022 = pd.read_csv('22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2022_monthly_totals.csv')

        # Read the CSV file that was created by the helper class from 2023
        df_2023 = pd.read_csv('22_23_WPI_converted_month_names_sorted_location_date_duplicates_sum_2023_monthly_totals.csv')

        # Concetenate the two years together
        df_combined = pd.concat([df_2022, df_2023])

        # Assings the value of the column 'TONNAGE' to the variable 'Tons'
        Tons = df_combined['TONNAGE']

        # Assings the value of the column 'Month' to the variable 'Month'
        Month = df_combined['Month']

        # Fit a polynomial to the data
        degree = 2  # Set the degree of the polynomial
        coefficients = np.polyfit(range(len(Tons)), Tons, degree)
        polynomial = np.poly1d(coefficients)

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
            legend_label='Polynomial Trend Line'
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

    def robot_recycling(self):
        pass

    def profitability(self):
        pass

    def roi(self):
        pass 

if __name__ == "__main__":
    # Run init
    Main().__init__

    # Graph the yearly charts
    #Main().WPI_Waste()

    # Graph the monthly charts
    #Main().WPI_Waste_Monthly()

    # Graph the academic year
    #Main().WPI_Waste_Academic_Year()

