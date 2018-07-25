# Application Name

Data Collector

# Application Overview

This application first collects user information (email address and age) and then emails back population statistics on age.

# Application Requirements

1. Python 3
2. PostgreSQL
3. Flask
4. Flask-SQLAlchemy
5. Psycopg2

# Application Usage

## First Time

1. Install PostgreSQL
2. Start the PostgreSQL service
3. Create a database in PostgreSQL called `data_collector`
4. Go to the directory `<path-to-python_applications>/data_collector`
5. Run `python`
6. Run `from app import db`
7. Run `db.create_all()`
8. Run `exit()`
9. Run `python app.py`

## Not the First Time

1. Start the PostgreSQL service
2. Run `python <path-to-python_applications>/data_collector/app.py`

# Some Application Improvements

1. Make the frontend more visually appealing.
2. Validate given email addresses.
3. Allow users to enter more useful data to calculate population statistics for them.
4. Deploy the application on Heroku (Cloud Application Platform). This allows everybody to access your application without having to run it locally.
