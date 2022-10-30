from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
   return "Hello World!!!"
if __name__ == '__main__':
    app.run()


# Flask is initially imported from flask module. A flask application is then initialised with expression app = Flask(__name__).

# __name__ is a predefined python variable holding name of the module, in which it is present, as it's value.

# A view function, hello is defined. It returns the message "Hello World!!!". This function is called when user accesses the URL /.

# Finally, the expression app.run() starts the web server at address : 127.0.0.1 and port 5000.