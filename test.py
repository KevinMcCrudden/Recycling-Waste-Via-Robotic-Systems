import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.io import output_file, show

# Specify the output file and title
output_file("recyclable_items_sorted_by_robot.html", title="Daily Recyclable Items Sorted by Robot")

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

# Assuming each month has 30 days for simplicity in this simulation
df_combined['DailyTonnage'] = df_combined['TONNAGE'] / 30

# Variables for the calculation
item_weight = 0.5 # Pounds
recycling_rate = 0.19 # 19% of items that can actually be recycled

# Calculate daily recyclable items
df_combined['DailyRecyclableItems'] = df_combined['DailyTonnage'] * 2000 / item_weight * recycling_rate

# Prepare data for Bokeh plotting
source = ColumnDataSource(df_combined)

# Create a Bokeh plot
plot = figure(title="Daily Recyclable Items Sorted by Robot", x_axis_type="datetime", width=800, height=400)
plot.line('Date', 'DailyRecyclableItems', source=source, legend_label="Daily Recyclable Items", color="green")
plot.circle('Date', 'DailyRecyclableItems', source=source, fill_color="white", size=8)

# Format the plot
plot.xaxis.formatter = DatetimeTickFormatter(months="%b %Y")
plot.xaxis.major_label_orientation = np.pi/4
plot.yaxis.axis_label = "Daily Recyclable Items"
plot.legend.location = "top_left"

# Show plot in notebook
show(plot)
