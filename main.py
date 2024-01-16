from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8]

output_file("index.html")

# Add plot
p = figure(
    title="Simple Bokeh plot",
    x_axis_label="x",
    y_axis_label="y",
)

# Render glyph
p.line(x, y, line_width=2)

# Show results
show(p)