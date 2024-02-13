from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure, curdoc

# Sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [6, 7, 2, 4, 5]}
source = ColumnDataSource(data=data)

# Create two plots
plot1 = figure(plot_width=400, plot_height=400, title="Plot 1")
plot1.circle('x', 'y', size=10, source=source)

plot2 = figure(plot_width=400, plot_height=400, title="Plot 2")
plot2.line('x', 'y', source=source)

# Create a slider widget
slider = Slider(start=0, end=10, value=1, step=1, title="Modifier")

# Define a callback function
def update_data(attrname, old, new):
    scale = slider.value
    new_data = {'x': [xi*scale for xi in data['x']], 'y': [yi*scale for yi in data['y']]}
    source.data = new_data

# Attach the callback to the slider
slider.on_change('value', update_data)

# Arrange plots and widgets in a layout
layout = column(slider, row(plot1, plot2))

# Add the layout to the current document
curdoc().add_root(layout)
