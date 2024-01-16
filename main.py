from bokeh.plotting import figure, output_file, show
import pandas

# Read in CSV
df = pandas.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']


output_file("index.html")

# Add plot
p = figure(
    y_range=car,
    plot_width=800,
    plot_height=600,
    title="Cars with Top Horsepower",
    x_axis_label="Horsepower",
)

# Render glyph
p.line(x, y, line_width=2)

# Show results
show(p)