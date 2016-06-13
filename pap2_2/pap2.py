import pandas as pd
import uncertainties as uc
import uncertainties.unumpy as un

from numpy import *
from scipy.optimize import curve_fit
from matplotlib.pyplot import *
from IPython.display import display, Latex, HTML
from prettytable import PrettyTable
from html import escape

import warnings
import itertools


def __init__():
    warnings.filterwarnings('ignore')

def chi2(data, fdata, err):
    """
    Calculate chi^2 for given data and fit
    """
    return sum(((data-fdata)/err)**2)


def pformat(data):
    if isinstance(data, str):
        return data
    elif hasattr(data, "__iter__"):
        return [pformat(i) for i in data]
    elif isinstance(data, uc.UFloat):
        return "${:L}$".format(data)
    else: return data


class Table(PrettyTable):
    """docstring for Table"""

    def __init__(self, title):
        super(Table, self).__init__()
        self._title = title

    def get_html_string(self, **kwargs):
        title = None
        if "title" in kwargs.keys():
            title = kwargs["title"]
            kwargs["title"] = ""
        if self.title:
            title = self.title
            self.title = ""
        html = super(Table, self).get_html_string(**kwargs).splitlines()
        if title:
            html.insert(1, "<h3>{0}</h3>".format(title))

        return "\n".join(html)


def display_table(table):
    if isinstance(table, Table):
        display(HTML(table.get_html_string()))
    else:
        display(table)

def display_latex(obj):
    if isinstance(obj, Latex):
        display(obj)
    else: display(Latex(obj))
