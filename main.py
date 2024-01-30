from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.models import Legend, ColumnDataSource, DataTable, TableColumn, LegendItem
import math
import pandas as pd
import helper as Helper

class Main:
    def __init__(self):
        # Initialize the class with many variables
        # Creates a variable to hold the csv file name
        raw_csv_file = '22_23_WPI.csv'

        # Create an instance of the helper class as Helper, using Tools to call it
        # Also brings in varialbles defined in the helper class
        self.Tools = Helper.MyClass()

        # Assings the value of the column 'MONTH' to the variable 'Month'
        # Also converts the list of numbers to a list of strings as Bokeh does not support integers
        raw_csv_file = self.Tools.convert_to_month_names(raw_csv_file)

        # Sorts the data by year and month
        raw_csv_file = self.Tools.sorter(raw_csv_file)

        # Combines the 'CUSTOMER_NM' column with the 'MONTH_STRING' column
        raw_csv_file = self.Tools.location_date(raw_csv_file)

        # Removes duplicate locations during the same month and totals the TONNAGE
        raw_csv_file = self.Tools.remove_duplicates_sum(raw_csv_file)

        # This splits the 2022 and 2023 years apart to graph them separately
        raw_csv_file = self.Tools.create_yearly_files(raw_csv_file)
    
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
        self.Tons_2022 = df_2022['TONNAGE']

        # Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year' for 2022
        self.Location_Date_Year_2022 = df_2022['Combined_Column']

        # Assings the value of the column 'TONNAGE' to the variable 'Tons' for 2022
        self.Tons_2023 = df_2023['TONNAGE']

        # Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year' for 2022
        self.Location_Date_Year_2023 = df_2023['Combined_Column']

        # Add plot for 2022 year
        f1 = figure(
            title="22 WPI Recycling",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=self.Location_Date_Year_2022,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
            
        )

        # Render glyph for 2022 year
        f1.vbar(
            x=self.Location_Date_Year_2022,
            top=self.Tons_2022,
            fill_alpha=0.5,
            line_color='green',
        )

        # Add plot for 2023 year
        f2 = figure(
            title="23 WPI Recycling",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=self.Location_Date_Year_2023,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
            
        )

        # Render glyph for 2023 year
        f2.vbar(
            x=self.Location_Date_Year_2023,
            top=self.Tons_2023,
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
        self.Tons_2022 = df_2022['TONNAGE']

        # Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year' for 2022
        self.Month_2022 = df_2022['Month']

        # Assings the value of the column 'TONNAGE' to the variable 'Tons' for 2022
        self.Tons_2023 = df_2023['TONNAGE']

        # Assings the value of the column 'Combined_Column' to the variable 'Location_Date_Year' for 2022
        self.Month_2023 = df_2023['Month']

        # Create a ColumnDataSource for the legend of 2022
        legend_source_2022 = ColumnDataSource(data=dict(Year=['2022'], Total=[df_2022['TONNAGE'].sum()]))

        # Create a ColumnDataSource for the legend of 2023
        legend_source_2023 = ColumnDataSource(data=dict(Year=['2023'], Total=[df_2023['TONNAGE'].sum()]))

        # Add plot for 2022 year
        f1 = figure(
            title="22 WPI Recycling Monthly",
            x_axis_label="Months of the year",
            y_axis_label="Weight in Tons",
            x_range=self.Month_2022,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
        )

        # Render glyph for 2022 year
        bar1 = f1.vbar(
            x=self.Month_2022,
            top=self.Tons_2022,
            fill_alpha=0.5,
            line_color='green',
            legend_label="2022"
        )

        # Create a legend for 2022
        legend_2022 = Legend(
            items=[("Total", [bar1])],
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
            x_range=self.Month_2023,
            tools="pan,box_select,zoom_in,zoom_out,save,reset",
            sizing_mode="stretch_both",
        )

        # Render glyph for 2023 year
        bar2 = f2.vbar(
            x=self.Month_2023,
            top=self.Tons_2023,
            fill_alpha=0.5,
            line_color='green',
            legend_label="2023"
        )

        # Create a legend for 2023
        legend_2023 = Legend(
            items=[("Total", [bar2])],
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
        plots = row([f1, f2], sizing_mode="stretch_both")

        # Show results
        show(plots)

        #    # Add plot for 2022 year
        # f1 = figure(
        #     title="22 WPI Recycling Monthly",
        #     x_axis_label="Months of the year",
        #     y_axis_label="Weight in Tons",
        #     x_range=self.Month_2022,
        #     tools="pan,box_select,zoom_in,zoom_out,save,reset",
        #     sizing_mode="stretch_both",
            
        # )

        # # Render glyph for 2022 year
        # bar1 = f1.vbar(
        #     x=self.Month_2022,
        #     top=self.Tons_2022,
        #     fill_alpha=0.5,
        #     line_color='green',
        #     legend_label="2022"
        # )

        # # Add plot for 2023 year
        # f2 = figure(
        #     title="23 WPI Recycling Monthly",
        #     x_axis_label="Months of the year",
        #     y_axis_label="Weight in Tons",
        #     x_range=self.Month_2023,
        #     tools="pan,box_select,zoom_in,zoom_out,save,reset",
        #     sizing_mode="stretch_both",
            
        # )

        # # Render glyph for 2023 year
        # bar2 = f2.vbar(
        #     x=self.Month_2023,
        #     top=self.Tons_2023,
        #     fill_alpha=0.5,
        #     line_color='green',
        #     legend_label="2023"
        # )

        # # Rotate the x-axis labels
        # f1.xaxis.major_label_orientation ="vertical"
        # f2.xaxis.major_label_orientation ="vertical"

        # # Combining plots 
        # plots = row([f1,f2], sizing_mode="stretch_both")

        # # Show results
        # show(plots)

if __name__ == "__main__":
    # Run init
    Main().__init__

    # Graph the yearly charts
    #Main().WPI_Waste()

    # Graph the monthly charts
    Main().WPI_Waste_Monthly()
