#!/usr/bin/env python3

# sys module
import os
import sys

# third parties module
import pandas as pd
import numpy as np
import matplotlib.cm as cm
from sklearn.datasets import fetch_20newsgroups

path_this = os.path.abspath (os.path.dirname (__file__))
def load_data (name):
    assert name.lower () in ('aggregation','compound','text'), 'Possible name: aggregation or compound'
    
    if name == 'aggregation':
        data = pd.read_csv (
            os.path.join (path_this, 'data', 'Aggregation.txt'), 
            delim_whitespace=True, 
            header=None, 
            names = ['x', 'y', 'cluster']
        )
    elif name == 'compound' :
        data = pd.read_csv (
            os.path.join (path_this, 'data', 'Compound.txt'), 
            delim_whitespace=True, 
            header=None, 
            names = ['x', 'y', 'cluster']
        )
    else:
        data_raw = fetch_20newsgroups (remove=('headers', 'footers', 'quotes'))
        data = pd.DataFrame ({'text' : data_raw['data'], 'cluster' : [data_raw['target_names'][i] for i in data_raw['target']]})
        return data
    
    return data

get_colors = lambda n: cm.rainbow(np.linspace(0, 1, n))


if __name__ == '__main__' :
    data = load_data ('compound')
