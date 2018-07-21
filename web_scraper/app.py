# Web Scraper Application

"""
Extracts Rock Springs Real Estate Property Data from Century 21's
Website, Formats the Data, and then Saves the data in a CSV File

Website:
https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/

Because Century 21's Website changes constantly, a cached version of the website is used for consistent results, regardless of when this application
is used. This version represents how the website looked at some point in time.

Cached Version of the Website:
https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
"""

# Import Modules
import requests
import pandas
from bs4 import BeautifulSoup



# Get First Webpage to Retrieve Total Number of Webpages

# GET Request to the Server to Receieve the HTML Document
first_page = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/").content

# Get BeautifulSoup object that represents the HTML Document as a Nested Data Structure for Simple Navigation 
first_page_soup = BeautifulSoup(first_page, "html.parser")

# Get Total Number of Webpages
pages = first_page_soup.find_all("a", {"class": "Page"})[-1].text



# Extract Data for all of the Real Estate Properties on Each Webpage

# List of Property Dictionaries
# Each Dictionary Contains a Property's Data as Key, Value Pairs
property_dictionary_list = []

# Base Format of the URL of Each Webpage
base_url = "https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=" 

# Loop through all of the Webpages of the Website 
for page in range(0, int(pages) * 10, 10):

    # GET Request to the Server to Receive the HTML Document
    web_page = requests.get(base_url + str(page) + ".html").content

    # Get BeautifulSoup object that represents the HTML Document as a Nested Data Structure for Simple Navigation 
    web_page_soup = BeautifulSoup(web_page, "html.parser")

    # Extract all of the Real Estate Properties in Full and Collect in a List
    # Each Real Estate Property belongs to a "div" Tag with Class "propertyRow"
    all_properties = web_page_soup.find_all("div", {"class": "propertyRow"})

    # Extract Data for Each Real Estate Property
    for single_property in all_properties:

        # Store Property's Data as Key, Value Pairs
        property_dictionary = {}

        # Extract the Address
        address = single_property.find_all("span", {"class": "propAddressCollapse"})[0].text
        property_dictionary["Address"] = address

        # Extract the Locality if it Exists
        locality = single_property.find_all("span", {"class": "propAddressCollapse"})[1]
        if locality != None:
            locality = locality.text
        property_dictionary["Locality"] = locality

        # Extract the Price
        price = single_property.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
        property_dictionary["Price"] = price

        # Extract the Area in Square Feet if it Exists
        area = single_property.find("span", {"class": "infoSqFt"})
        if area != None:
            area = area.find("b").text
        property_dictionary["Area"] = area
    
        # Extract the Number of Beds if it Exists
        beds = single_property.find("span", {"class": "infoBed"})
        if beds != None:
            beds = beds.find("b").text
        property_dictionary["Beds"] = beds

        # Extract the Number of Full Baths if it Exists
        full_baths = single_property.find("span", {"class": "infoValueFullBath"})
        if full_baths != None:
            full_baths = full_baths.find("b").text
        property_dictionary["Full Baths"] = full_baths

        # Extract the Number of Half Baths if it Exists
        half_baths = single_property.find("span", {"class": "infoValueHalfBath"})
        if half_baths != None:
            half_baths = half_baths.find("b").text
        property_dictionary["Half Baths"] = half_baths

        # Extract the Lot Size if it Exists
        # The Lot Size is tricky because there are multiple "span" Tags with Class "featureGroup" that contain features other than Lot Size
        for column_group in single_property.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    property_dictionary["Lot Size"] = feature_name.text

        # Add Dictionary to List of Property Dictionaries
        property_dictionary_list.append(property_dictionary)

# Create DataFrame object out of List of Property Dictionaries
data_frame = pandas.DataFrame(property_dictionary_list)

# Add Extracted Real Estate Property Data to a CSV File
data_frame.to_csv("real_estate_property_data.csv")
