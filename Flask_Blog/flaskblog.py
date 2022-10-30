# https://flask.palletsprojects.com/en/2.2.x/quickstart/

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Home Page</p>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"


# below if works only if we run from python directly if we want to run it from another module we need to use variables as mentioned below
if __name__ == '__main__':
    # app.run()
    app.run(debug=True,host="0.0.0.0",port=1000)

# To Run in mac/linux
# export FLASK_APP=flaskblog.py
# in windows
# set FLASK_APP=flaskblog.py
# Run in debug mode to see live changes
# set FLASK_DEBUG=1
# flask run -p 5001