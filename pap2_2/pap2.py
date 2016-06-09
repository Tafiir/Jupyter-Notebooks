import pandas as pd
import uncertainties as uc
import uncertainties.unumpy as un

from numpy import *
from scipy.optimize import curve_fit
from matplotlib.pyplot import *
from IPython.display import *

import warnings


def __init__():
    warnings.filterwarnings('ignore')

def chi2(data, fdata, err):
    """
    Calculate chi^2 for given data and fit
    """
    return sum(((data-fdata)/err)**2)

class Table(object):
    """
    HTML Table Class
    """
    def __init__(self):
        pass #TODO: Run real __init__ function with filler values

    #TODO: Implement

def display_table():
    #TODO: Implement
    pass
