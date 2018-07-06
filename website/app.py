from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page Goes Here!"

@app.route('/about')
def about():
    return "About Page Goes Here!"

if __name__ == "__main__":
    app.run(debug = True)
