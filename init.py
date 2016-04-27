from numpy import *
from matplotlib.pyplot import *
import pandas as pd
import scipy as sp
import sympy as sm
from IPython.display import display, Latex, Math, Markdown, HTML
import warnings

version = "2.0.0"

def init():
    warnings.filterwarnings('ignore')

def to_valerr(id, val, err, r=-1, unit=""):
    if r != -1:
        val = float64(val).round(r)
        err = float64(err).round(r)

    if unit is "":
        return r"${0} = {1} \pm {2}$".format(id, val, err)
    else:
        return r"${0} = {1} \pm {2} \ {3}$".format(id, val, err, unit)

def display_valerr(valerr):
    display(Latex(valerr))

def chi2(data, fdata, err):
    return sum(((data-fdata)/err)**2)

def display_valtable(keyvals):
    tables = []
    for key, val in keyvals:
        tables.append("<tr><td>{0}</td><td>{1}</td></tr>".format(key, val))
    display(HTML('<table>{}</table>'.format("".join(tables))))
