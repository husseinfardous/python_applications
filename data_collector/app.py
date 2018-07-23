# Data Collector Application

# Collects User Information (Email Address and Age) and then Emails back Population Statistics on Age

# Import Modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



# Configure Flask and Connect to PostgreSQL Database "data_collector"

# Create an Instance of Flask Class for the Web Application
app = Flask(__name__)

# Connect Flask to PostgreSQL Database "data_collector"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/data_collector"

# Create SQLAlchemy object
# SQLAlchemy facilitates Interaction between Flask and PostgreSQL
db = SQLAlchemy(app)

# Create Class that Represents Blueprint of Data to Collect
# Inherit from SQLAlchemy Model Class
class Data(db.Model):

    # Create a Table called "data"
    # Add Three Columns to the Table: id, email, and age
    # The Three Columns are the Data Class' Properties
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True)
    age = db.Column(db.Integer)

    # Initialize Properties
    def __init__(self, email, age):
        self.email = email
        self.age = age

# Display User Submission Webpage
@app.route("/")
def index():
    return render_template("index.html")

# Capture POST Data (Email Address and Age)
# Store POST Data in Database "data_collector" if Email Address is Unique
# Display Success Webpage if Email Address is Unique
# Display User Submission Webpage again if Email Address is not Unique
@app.route("/success", methods = ["POST"])
def success():

    if request.method == "POST":

        email = request.form["email"]
        age = request.form["age"]

        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, age)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")

    return render_template("index.html", text = "Sorry, that Email Address was Used Already!")



# main() Function
# Condition ensures that Web Application runs only if this module is run interactively
# Web Application won't run if this module is imported into another module
if __name__ == "__main__":
    app.debug = True
    app.run(port = 3000)
