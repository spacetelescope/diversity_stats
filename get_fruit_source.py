from bokeh.models import ColumnDataSource, FactorRange, Range1d 
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import read_data

def get_fruit_data(): 

    palette = ["#c9d9d3", "#718dbf", "#e84d60", "green", "red","orange"]
    fruits = ['Colloquium', 'Hiring', 'Workshops', 'RIAs', 'Grapes', 'Strawberries']
    years = ['2015', '2016', '2017', '2018']
    data = {'fruits' : fruits,
            '2015'   : [2, 1, 4, 3, 2, 4],
            '2016'   : [5, 3, 3, 2, 4, 6],
            '2017'   : [3, 2, 4, 4, 5, 3],
            '2018'   : [3, 1, 1, 3, 1, 3]}
    palette = ["#c9d9d3", "#718dbf", "#e84d60", "green"]
    
    # this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
    x = [ (fruit, year) for fruit in fruits for year in years ]
    counts = sum(zip(data['2015'], data['2016'], data['2017'], data['2018']), ()) # like an hstack
    source = ColumnDataSource(data=dict(x=x, counts=counts))
 
    return source 
