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

import os

import numpy as np
from astropy.io import ascii as asc
from bokeh.models import ColumnDataSource

DATA_DIR = os.path.abspath('data')


class SRC_data():
    '''Load and format data about SRC hiring
    '''
    def __init__(self):
        # Load data from CSV file
        file = os.path.join(DATA_DIR, 'SRC_stats_2012.csv')
        self.data = asc.read(file)

        # Define axes
        self.years = ['2012', '2014', '2016']
        self.genders = ['Male', 'Female', 'Non-Binary']

        # Create tuples for every combination of year and gender
        self.x = [(year, gender) for year in self.years for gender in self.genders]

    def get_data(self, stage):
        # Possible stages include 'pool', 'long-list', 'short-list', 'hire'
        if stage not in ['pool', 'long-list', 'short-list', 'hire']:
            return ValueError("Invalid state {}; must be one of 'pool', 'long-list', 'short-list', 'hire'".format(stage))
        self.data = {'years': self.years,
                     'Male': self.data['{} M'.format(stage)],
                     'Female': self.data['{} F'.format(stage)],
                     'Non-Binary': [0]*3}

    def create_columns(self):
        '''Create ColumnDataSource for nested Bokeh bar plot
        '''
        # Create an hstack of the data
        counts = sum(zip(self.data['Male'],
                         self.data['Female'],
                         self.data['Non-Binary']),
                     ())
        source = ColumnDataSource(data=dict(x=self.x, counts=counts))
        return source


class science_evaluation_data():
    '''Load and format data about science evaluations
    '''
    def __init__(self):
        # Load data from CSV file
        file = os.path.join(DATA_DIR, 'Science_Evals_SEC.csv')
        self.data = asc.read(file)

        # Define axes
        self.years = ['2013', '2014', '2015', '2016', '2017']
        self.genders = ['Male', 'Female', 'Non-Binary']

        # Create tuples for every combination of year and gender
        self.x = [(year, gender) for year in self.years for gender in self.genders]

    def get_data(self, level):
        # Levels range from 1 to 4
        if str(level) not in ['1', '2', '3', '4']:
            return ValueError("Invalid state {}; must be between 1 and 4".format(level))
        self.data = {'years': self.years,
                     'Male': self.data['Level {} Male'.format(level)],
                     'Female': self.data['Level {} Female'.format(level)],
                     'Non-Binary': [0]*5}

    def create_columns(self):
        '''Create ColumnDataSource for nested Bokeh bar plot
        '''
        # Create an hstack of the data
        counts = sum(zip(self.data['Male'],
                         self.data['Female'],
                         self.data['Non-Binary']),
                     ())
        source = ColumnDataSource(data=dict(x=self.x, counts=counts))
        return source


class research_staff_data():
    '''Load and format data about research staff
    '''
    def __init__(self):
        # Load data from CSV file
        file = os.path.join(DATA_DIR, 'Research_staff_stats.csv')
        self.data = asc.read(file)

        # Define axes
        self.years = np.arange(1980, 2018).astype(str)
        self.genders = ['Male', 'Female', 'Non-Binary']

        # Create tuples for every combination of year and gender
        self.x = [(year, gender) for year in self.years for gender in self.genders]

    def get_data(self, data_type):
        # Possible types include 'Hire' and 'Left'
        if data_type not in ['Hire', 'Left']:
            return ValueError("Invalid type {}; must be either 'Hire' or 'Left'".format(data_type))
        self.data = {'years': self.years,
                     'Male': self.data['{} male'.format(data_type)],
                     'Female': self.data['{} female'.format(data_type)],
                     'Non-Binary': [0]*5}

    def create_columns(self):
        '''Create ColumnDataSource for dodged Bokeh bar plot
        '''
        source = ColumnDataSource(data=self.data)
        return source


class renewal_promotion_data():
    '''Load and format data about renewal and promotions
    '''
    def __init__(self):
        # Load data from CSV file
        file = os.path.join(DATA_DIR, 'Renewal_Promotion_SPC.csv')
        self.data = asc.read(file)

        # Define axes
        self.years = ['2013', '2014', '2015', '2016', '2017']
        self.genders = ['Male', 'Female', 'Non-Binary']

        # Create tuples for every combination of year and gender
        self.x = [(year, gender) for year in self.years for gender in self.genders]

    def get_data(self, data_type):
        # Possible types include 'Renewal', 'Promotion', and 'Cases'
        if data_type not in ['Renewal', 'Promotion', 'Cases']:
            return ValueError("Invalid type {}; must be either 'Renewal', 'Promotion', or 'Cases'".format(data_type))
        self.data = {'years': self.years,
                     'Male': self.data['{} Male'.format(data_type)],
                     'Female': self.data['{} Female'.format(data_type)],
                     'Non-Binary': [0]*5}

    def create_columns(self):
        '''Create ColumnDataSource for nested Bokeh bar plot
        '''
        # Create an hstack of the data
        counts = sum(zip(self.data['Male'],
                         self.data['Female'],
                         self.data['Non-Binary']),
                     ())
        source = ColumnDataSource(data=dict(x=self.x, counts=counts))
        return source
