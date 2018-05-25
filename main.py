from bokeh.io import show, output_file
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, FactorRange, Range1d 
from bokeh.layouts import column, row, widgetbox
from bokeh.models.widgets import Slider, TextInput, Select, Tabs, Panel, Div
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

import read_data
import get_hiring_plot as g 
import get_sec_plot as s 
import get_fruit_source as gf 
import get_generic_plot as gg 

palette = ["#c9d9d3", "#718dbf", "#e84d60", "green"]

def get_generic_plot(): 
    fruit_source = gf.get_fruit_data() 
    years = ['2015', '2016', '2017', '2018'] 
    p = figure(x_range=FactorRange(*fruit_source.data['x']), plot_height=350, plot_width=500, title="                   ",
               toolbar_location='right', tools=["pan,reset,tap,wheel_zoom,save"]) 
    p.vbar(x='x', top='counts', width=0.9, source=fruit_source, line_color="white",
           fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2))
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    return p 

colloq_plot = get_generic_plot() 
hiring_plot, src_cds = g.get_hiring_plot('pool') 
sec_plot = s.get_sec_plot() 
spc_plot = get_generic_plot() 
isr_plot = get_generic_plot() 
staff_plot = get_generic_plot() 
meeting_plot = get_generic_plot() 

# HIRING PANEL 
hiring_category = Select(title="Hiring Stage", value="Pool", width=100, \
                options=["pool",  "long-list", "short-list", "hire"]) 
c = column(children=[hiring_category, hiring_plot])  
hiring_panel = Panel(child=c, title='Hiring', width=300)

def update_data(attrname, old, new): 
   print('you want category', new, ' but we do not have that yet!') 
   _, src_cds_new = g.get_hiring_plot(new) 
   src_cds.data = src_cds_new.data 
   #print('you want category', new, ' but we do not have that yet!') 
   
for w in [hiring_category]:  w.on_change('value', update_data)

colloq_panel = Panel(child=colloq_plot, title='Colloquium', width=300)
sec_evals = Panel(child=sec_plot, title='SEC Evals', width=300)
spc_evals = Panel(child=spc_plot, title='SPC Reviews', width=300)
isr_authors = Panel(child=isr_plot, title='ISR Authors', width=300)
staff = Panel(child=staff_plot, title='Staff Comp', width=300)
meetings = Panel(child=meeting_plot, title='Meeting Speakers', width=300)

tabs = Tabs(tabs=[ colloq_panel, hiring_panel, sec_evals, spc_evals, isr_authors, staff, meetings], width=500) 

curdoc().add_root(tabs)





