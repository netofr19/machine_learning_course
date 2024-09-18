from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this amazing Flask Course."

@app.route("/index")
def index():
    return "Wlcome to the index page"

if __name__ == "__main__":
    app.run(debug=True)
