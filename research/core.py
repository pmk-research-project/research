# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['TimeSeriesTypes', 'TimeSeries', 'Ledger', 'foo']

# %% ../nbs/00_core.ipynb 2
import typing as ta
from enum import Enum

import pandas as pd

# %% ../nbs/00_core.ipynb 3
class TimeSeriesTypes(Enum):
    """
    The type of TimeSeries object.
    """
    PRICES = "prices"
    TRADES = "trades"

class TimeSeries:
    """
    Creates a time series object that can access a plethora of financial 
    """
    def __init__(self, time_index: pd.Series, data: pd.Series, type: TimeSeriesTypes = "price"):
        self.ti = time_index
        self.d = data

# %% ../nbs/00_core.ipynb 5
class Ledger:
    """
    A class ledger API giving user access to accounting calculations.
    """
    def __init__(self, on_disk_path: str):
        self.p = on_disk_path

    def sync(self):
        pass 

# %% ../nbs/00_core.ipynb 7
def foo(): pass
