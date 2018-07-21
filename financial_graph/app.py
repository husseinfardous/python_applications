# Financial Graph Application

# Creates an Interactive Candlestick Chart of Stock Market Data



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
from bokeh.plotting import figure, show, output_file
import datetime as dt



# Return Trend of Stock Market Price for the Day
def trend(opening, closing):
    if opening > closing:
        value = "Decrease"
    elif opening < closing:
        value = "Increase"
    else:
        value = "Equal"
    return value



# Retrieve Google Stock Market Data
yf.pdr_override()
data_frame = pdr.get_data_yahoo(tickers = "GOOG", start = dt.datetime(2016, 3, 1), end = dt.datetime(2016, 3, 10))

# Add Column in DataFrame object that Describes the Trend of the Stock Market Price for the Day
data_frame["Trend"] = [trend(opening, closing) for opening, closing in zip(data_frame.Open, data_frame.Close)]

# Add Column in DataFrame object that Shows the Average of the Opening and Closing Stock Market Prices for the Day
data_frame["Average"] = (data_frame.Open + data_frame.Close) / 2

# Add Column in DataFrame object that Shows the Magnitude of the Difference between the Opening and Closing Stock Market Prices for the Day
data_frame["Height"] = abs(data_frame.Open - data_frame.Close)



# Create and Configure Interactive Candlestick Chart

# Create Interactive Candlestick Chart
chart = figure(x_axis_type = "datetime", height = 300, width = 1000)
chart.title.text = "Stock Market Candlestick Chart"

# Plot Bokeh Rectangles of Days in which Stock Opening Price > Stock Closing Price

# X-Axis
x_axis = data_frame.index[data_frame.Trend == "Decrease"]

# Y-Axis
y_axis = data_frame.Average[data_frame.Trend == "Decrease"]

# Height
height = data_frame.Height[data_frame.Trend == "Decrease"]

# Width
hours = 12
width = hours * 60 * 60 * 1000

# Plot
chart.rect(x = x_axis, y = y_axis, width = width, height = height, fill_color = "red", line_color = "black")

# Plot Bokeh Rectangles of Days in which Stock Opening Price < Stock Closing Price

# X-Axis
x_axis = data_frame.index[data_frame.Trend == "Increase"]

# Y-Axis
y_axis = data_frame.Average[data_frame.Trend == "Increase"] 

# Height
height = data_frame.Height[data_frame.Trend == "Increase"]

# Width
hours = 12
width = hours * 60 * 60 * 1000

# Plot
chart.rect(x = x_axis, y = y_axis, width = width, height = height, fill_color = "orange", line_color = "black")



# Save Interactive Candlestick Chart in an HTML File
output_file("financial_graph.html")
show(chart)
