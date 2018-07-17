# Web Scraper Application

"""
Extracts Rock Springs Real Estate Property Data from Century 21's
Website, Formats the Data, and then Saves the data in a CSV File

Website:
https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/

Because Century 21's Website changes constantly, a cached version of the website is used for consistent results, regardless of when this application
is used. This version represents how the website looked at some point in time.

Cached Version of the Website:
https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
"""

# Import Modules
import requests
from bs4 import BeautifulSoup



# Load First Page

# GET Request to the Server to Receive the HTML Document
first_page = requests.get("https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/").content

# Get BeautifulSoup object that represents the HTML Document as a Nested Data Structure for Simple Navigation 
first_page_soup = BeautifulSoup(first_page, "html.parser")
