#!/usr/bin/env python
'''Load demographic data and format into Bokeh-compatible form

Authors
-------
    - Lauren Chambers

Use
---
    ::
    import read_data
    SRC = read_data.SRC_data()
    SRC.get_data('pool')
    cols = SRC.create_columns()

References
----------
    Data formatted to match Bokeh bar plot example, located here:
    http://bokeh.pydata.org/en/latest/docs/gallery/bar_nested_colormapped.html

Notes
-----
    Created as a part of STScI "Hack the 'Tute" Day, May 25, 2018
'''

import numpy as np
from astropy.io import ascii as asc
from bokeh.models import ColumnDataSource


class SRC_data():
    '''Load and format data about SRC hiring
    '''
    def __init__(self):
        # Load data from CSV file
        self.data = asc.read('data/SRC_stats_2012.csv')

        # Define axes
        self.years = ['2012', '2014', '2016']
        self.genders = ['Male', 'Female', 'Non-Binary']

        # Create tuples for every combination of year and gender
        self.x = [(year, gender) for year in self.years for gender in self.genders]

    def get_data(self, stage):
        # Possible stages include 'pool', 'long-list', 'short-list', 'hire'
        self.data = {'years': self.years,
                     'Male': self.data['{} M'.format(stage)],
                     'Female': self.data['{} M'.format(stage)],
                     'Non-Binary': [np.nan]*3}

    def create_columns(self):
        # Create an hstack of the data
        counts = sum(zip(self.data['Male'],
                         self.data['Female'],
                         self.data['Non-Binary']),
                     ())
        source = ColumnDataSource(data=dict(x=self.x, counts=counts))
        return source
