from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row
import pandas

# Read in CSV
df = pandas.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']

# Add plot for orange cars
p = figure(
    y_range=car,
    width=800,
    height=600,
    title="Cars with Top Horsepower",
    x_axis_label="Horsepower",
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph for orange cars
p.hbar(
    y=car,
    right=hp,
    left=0,
    height=0.4,
    color="orange",
    fill_alpha=0.5
)

# Add plot for green cars
g = figure(
    y_range=car,
    width=800,
    height=600,
    title="Cars with Top Horsepower",
    x_axis_label="Horsepower",
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph for green cars
g.hbar(
    y=car,
    right=hp,
    left=0,
    height=0.4,
    color="green",
    fill_alpha=0.5
)

# Show results
show(column(p, g))