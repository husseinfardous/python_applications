# Website Application

# Displays a Basic Website on "localhost:5000"
# Gives Blueprints for Displaying a Website using Flask

# Import Modules
from flask import Flask, render_template



# Configure Flask

# Create an Instance of Flask Class for the Web Application
app = Flask(__name__)

# Display Home Webpage
@app.route("/")
def home():
    return render_template("home.html")

# Display About Webpage
@app.route("/about")
def about():
    return render_template("about.html")



# main() Function
# Condition ensures that Web Application runs only if this module is run interactively
# Web Application won't run if this module is imported into another module
if __name__ == "__main__":
    app.run(debug = True)
