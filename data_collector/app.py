# Data Collector Application

# Collects User Information (Email Address and Age) and then Emails back Population Statistics on Age

# Import Modules
from flask import Flask, render_template, request



# Configure Flask

# Create an Instance of Flask Class for the Web Application
app = Flask(__name__)

# Display User Submission Webpage
@app.route("/")
def index():
    return render_template("index.html")

# Capture POST Data (Email Address and Age)
# Display Success Webpage
@app.route("/success", methods = ["POST"])
def success():
    if request.method == "POST":
        email = request.form["email"]
        age = request.form["age"]
        return render_template("success.html")



# main() Function
# Condition ensures that Web Application runs only if this module is run interactively
# Web Application won't run if this module is imported into another module
if __name__ == "__main__":
    app.debug = True
    app.run(port = 3000)
