import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.io import output_file, show

def test():
    # Variables for the caluclation
    robot_rate = 960 # Items per day
    item_weight = 0.5 # Pounds
    recycling_rate = 0.19 # 19% of items that can actually be recycled
    
    # Simulated data creation
    dates_2022 = pd.date_range(start="2022-01-01", end="2022-12-31", freq='M')
    dates_2023 = pd.date_range(start="2023-01-01", end="2023-12-31", freq='M')
    tonnage = np.random.uniform(50, 150, size=(len(dates_2022) + len(dates_2023))) # Random tonnage between 50 and 150 tons

    # Correcting the concatenation mistake by converting DatetimeIndex to list
    dates_combined = pd.concat([pd.Series(dates_2022), pd.Series(dates_2023)]).reset_index(drop=True)

    # Correct DataFrame creation
    df_combined = pd.DataFrame({
        'Date': dates_combined,
        'TONNAGE': tonnage
    })

    # Assuming a total of 700 tons for the academic years
    total_tonnage = 700

    # Number of months across the two years
    num_months = len(dates_2022) + len(dates_2023)

    # Evenly distribute the total tonnage across all months
    tonnage_per_month = total_tonnage / num_months

    # Assign the tonnage per month to each month in the DataFrame
    df_combined['TONNAGE'] = tonnage_per_month

    # Recalculate daily tonnage based on the new tonnage values
    df_combined['DailyTonnage'] = df_combined['TONNAGE'] / 30

    # Recalculate daily recyclable items based on the initial recycling rate
    df_combined['DailyRecyclableItems'] = df_combined['DailyTonnage'] * 2000 / item_weight * recycling_rate

    # Prepare data for Bokeh plotting
    source = ColumnDataSource(df_combined)

    # Update the data source with the new calculations
    source.data = ColumnDataSource.from_df(df_combined)

    # Assuming each month has 30 days for simplicity in this simulation
    df_combined['DailyTonnage'] = df_combined['TONNAGE'] / 30

    # Variables for the calculation
    item_weight = 0.5 # Pounds
    recycling_rate = 0.19 # 19% of items that can actually be recycled

    # Calculate daily recyclable items
    df_combined['DailyRecyclableItems'] = df_combined['DailyTonnage'] * 2000 / item_weight * recycling_rate

    # Create a Bokeh plot
    plot = figure(title="Daily Recyclable Items Sorted by Robot", x_axis_type="datetime", width=800, height=400)
    plot.line('Date', 'DailyRecyclableItems', source=source, legend_label="Daily Recyclable Items", color="green")
    plot.circle('Date', 'DailyRecyclableItems', source=source, fill_color="white", size=8)

    # Format the plot
    plot.xaxis.formatter = DatetimeTickFormatter(months="%b %Y")
    plot.xaxis.major_label_orientation = np.pi/4
    plot.yaxis.axis_label = "Daily Recyclable Items"
    plot.legend.location = "top_left"

    # Create sliders
    recycling_rate_slider = Slider(start=0, end=1, value=0.19, step=0.01, title="Recycling Rate")
    num_robots_slider = Slider(start=1, end=10, value=1, step=1, title="Number of Robots")
    downtime_slider = Slider(start=0, end=100, value=0, step=1, title="Robot Downtime (%)")

    # Define the update function to use the new tonnage values
    def update(attr, old, new):
        # Adjust recycling rate based on slider
        recycling_rate = recycling_rate_slider.value
        
        # Adjust for number of robots
        num_robots = num_robots_slider.value
        
        # Adjust for downtime
        downtime_adjustment = 1 - (downtime_slider.value / 100)
        
        # Recalculate daily recyclable items with the new parameters
        new_daily_recyclable_items = df_combined['DailyTonnage'] * 2000 / item_weight * recycling_rate * num_robots * downtime_adjustment
        source.data['DailyRecyclableItems'] = new_daily_recyclable_items

    # Ensure to reattach the update function if it's defined before this point
    recycling_rate_slider.on_change('value', update)
    num_robots_slider.on_change('value', update)
    downtime_slider.on_change('value', update)

    # Layout setup
    layout = column(plot, recycling_rate_slider, num_robots_slider, downtime_slider)

    return layout
