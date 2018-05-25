from bokeh.models import ColumnDataSource, FactorRange, Range1d 
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import read_data

palette = ["#c9d9d3", "#718dbf", "#e84d60", "green"]

def get_hiring_plot(stage):

    SRC = read_data.SRC_data()
    SRC.get_data(stage)
    src_cds = SRC.create_columns()

    p = figure(x_range=FactorRange(*src_cds.data['x']), plot_height=350, plot_width=500, title="               ",
               toolbar_location='right', tools=["pan,reset,tap,wheel_zoom,save"]) 

    p.vbar(x='x', top='counts', width=0.9, source=src_cds, line_color="white",
           fill_color=factor_cmap('x', palette=palette, factors=['2012', '2014', '2016'], start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = 'white'
    return p, src_cds 
