# Financial Graph Application

# Creates an Interactive Graph of Stock Market Data



# Import Modules

"""
"pandas_datareader" requires "is_list_like" and imports it from "pandas.core.common", but "is_list_like" was moved to "pandas.api.types".

Temporary Fix: Set "pandas.core.common.is_list_like" equal to "pandas.api.types.is_list_like".

Permanent Fix: pandas_datareader version 0.7.0 will fix this issue.
"""

# The two lines below are unncessary in pandas_datareader version >= 0.7.0
import pandas
pandas.core.common.is_list_like = pandas.api.types.is_list_like

# Yahoo! Finance decommissioned their Data API
# This module temporarily fixes the issue by "scraping" the data from Yahoo! Finance
import fix_yahoo_finance as yf

from pandas_datareader import data as pdr
import datetime as dt



# Retrieve Google Stock Market Data
yf.pdr_override()
data_frame = pdr.get_data_yahoo(tickers = "GOOG", start = dt.datetime(2018, 7, 1), end = dt.datetime(2018, 7, 10))
