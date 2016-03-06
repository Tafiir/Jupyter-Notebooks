from numpy import *
from matplotlib.pyplot import *
import pandas as pd
import scipy as sp
import sympy as sm
from IPython.display import display, Latex, Math
import warnings

def init():
    warnings.filterwarnings('ignore')

def valerr(id, val, err, r=-1, unit=""):
    if r != -1:
        val = float64(val).round(r)
        err = float64(err).round(r)

    if unit is "":
        display(Latex(r"${0} = {1} \pm {2}$".format(id, val, err)))
    else:
        display(Latex(r"${0} = {1} \pm {2} \ {3}$".format(id, val, err, unit)))
