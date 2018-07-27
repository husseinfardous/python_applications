# Geocoder Application

# Collects Addresses and then Converts them into Latitude/Longitude Coordinates 

# Import Modules
from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas
import datetime



# Configure Flask

# Create an Instance of Flask Class for the Web Application
app = Flask(__name__)

# Display User Submission Webpage
@app.route("/")
def index():
    return render_template("index.html")

# On Success, Display User Submission Webpage with the DataFrame object that contains the Latitude/Longitude Coordinates and a Download Button
# On Failure, Display User Submission Webpage with the Error that Occurred
@app.route("/success-table", methods = ["POST"])
def success_table():

    global filename

    if request.method == "POST":

        # Capture POST Data (CSV File)
        file = request.files["file"]

        try:

            # Create DataFrame object from CSV File
            data_frame = pandas.read_csv(file)

            # Create Geocoder object
            geocoder = Nominatim(scheme = "http")

            # Add "coordinates" Column in DataFrame that Contains Geographical Coordinates of the Addresses
            data_frame["coordinates"] = data_frame["Address"].apply(geocoder.geocode)

            # Add "Latitude" and "Longitude" Columns in DataFrame
            # Latitude and Longitude Values are Retrieved from "coordinates" Column
            data_frame["Latitude"] = data_frame["coordinates"].apply(lambda x: x.latitude if x != None else None)
            data_frame["Longitude"] = data_frame["coordinates"].apply(lambda x: x.longitude if x != None else None)
            
            # Delete "coordinates" Column in DataFrame
            data_frame = data_frame.drop("coordinates", 1)

            # Convert DataFrame to a CSV File
            filename = datetime.datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
            data_frame.to_csv(filename, index = None)

            # Display User Submission Webpage, DataFrame object, and Download Button
            return render_template("index.html", text = data_frame.to_html(), btn = "download.html")

        # Exception Occurred
        except Exception as e:

            # Display User Submission Webpage with the Error that Occurred
            return render_template("index.html", text = str(e))

# Send CSV File to Users when Download Button is Clicked
@app.route("/download-file/")
def download():
    return send_file(filename, attachment_filename = "yourfile.csv", as_attachment = True)



# main() Function
# Condition ensures that Web Application runs only if this module is run interactively
# Web Application won't run if this module is imported into another module
if __name__ == "__main__":
    app.run(debug = True)
