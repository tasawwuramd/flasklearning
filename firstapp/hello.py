import imp
from flask import Flask
from flask import redirect
app = Flask(__name__)
@app.route("/")
def hello():
   return "Hello World!!!"

# Using Variable rules


@app.route("/user/<username>/")
def hello_user(username):
    return "Hello " + username + "!!!"

@app.route("/user/<username>/<int:age>/")
def display_age(username, age):
    print(age)
    print(type(age)) #printed in the terminal
    return "Hello " + username +"!!!<br>You are " + str(age) + " years old. Variable default type captured is:" + str(type(age))


@app.route("/home/")
def demo_redirect():
    return redirect("http://localhost:5000/")


from flask import redirect, url_for



@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('hello_user', username=uname))  #here hello user is method to which the username needs to be sent


if __name__ == '__main__':
    app.run()


# Flask is initially imported from flask module. A flask application is then initialised with expression app = Flask(__name__).

# __name__ is a predefined python variable holding name of the module, in which it is present, as it's value.

# A view function, hello is defined. It returns the message "Hello World!!!". This function is called when user accesses the URL /.

# Finally, the expression app.run() starts the web server at address : 127.0.0.1 and port 5000.


# The rule parameter value, / binds the URL / to hello view function using route decorator.
# Hence if a user visits the URL http://localhost:5000/, the output of hello function is shown in the browser, to the user.