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



# Extract Data for all of the Real Estate Properties on the First Page

# GET Request to the Server to Receive the HTML Document
first_page = requests.get("https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/").content

# Get BeautifulSoup object that represents the HTML Document as a Nested Data Structure for Simple Navigation 
first_page_soup = BeautifulSoup(first_page, "html.parser")

# Extract all of the Real Estate Properties in Full and Collect in a List
# Each Real Estate Property belongs to a "div" Tag with Class "propertyRow"
all_properties = first_page_soup.find_all("div", {"class": "propertyRow"})

# Extract Data for Each Real Estate Property
for single_property in all_properties:

    # Extract the Price
    price = single_property.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
    print(price)

    # Extract the Address
    address_first_half = single_property.find_all("span", {"class": "propAddressCollapse"})[0].text
    print(address_first_half)
    address_second_half = single_property.find_all("span", {"class": "propAddressCollapse"})[1].text
    print(address_second_half)

    # Extract the Number of Beds if it Exists
    beds = single_property.find("span", {"class": "infoBed"})
    if beds != None:
        beds = beds.find("b").text
    print(beds)

    # Extract the Area in Square Feet if it Exists
    area = single_property.find("span", {"class": "infoSqFt"})
    if area != None:
        area = area.find("b").text
    print(area)

    # Extract the Number of Full Baths if it Exists
    full_baths = single_property.find("span", {"class": "infoValueFullBath"})
    if full_baths != None:
        full_baths = full_baths.find("b").text
    print(full_baths)

    # Extract the Number of Half Baths if it Exists
    half_baths = single_property.find("span", {"class": "infoValueHalfBath"})
    if half_baths != None:
        half_baths = half_baths.find("b").text
    print(half_baths)

    # Extract the Lot Size if it Exists
    # The Lot Size is tricky because there are multiple "span" Tags with Class "featureGroup" that contain features other than Lot Size
    for column_group in single_property.find_all("div", {"class": "columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
            if "Lot Size" in feature_group.text:
                print(feature_name.text)

    print("")
