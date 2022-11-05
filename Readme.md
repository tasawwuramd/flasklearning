https://flask.palletsprojects.com/en/2.2.x/quickstart/
Fresco Flask

1)

Flask is based on the Web Server Gateway Interface toolkit, and the Jinja2 templating engine.
The Jinja2 templating engine is a popular Python web templating system that combines templates and data sources to render dynamic web pages.

About Course

In this course, you will study the following topics about Flask framework.
Setting up an isolated environment for a Python project.
Installation of Flask and some of its extensions.
Developing a basic Flask application
How Flask handles web requests
Using templates as a presentation layer
Connecting to a Database
Creating web forms

Isolating Project Dependencies
A virtual environment is an isolated environment, which holds all dependencies of a project.

A virtual environment separates the project dependencies from global run time environment.

Hence, adding new or upgrading existing dependencies in a virtual environment doesn't have any effect on the original dependencies, present in the global environment.

A virtual environment provides a complete freedom to manage packages required for an application.

Also a virtual environments is owned by the user, who created it and do not require administrator privileges.


Creating a Virtual Environment
Support for creation of a virtual environment is included by default in Python version 3.4 and above.

You can create a virtual environment using venv module, while using python 3.4 and above, as shown in below command.
$ python3 -m venv projenv

While using older versions of python, installation of the third-party module, virtualenv is required for creating a virtual environment.

After successful installation of virtualenv, you can create a virtual environment as shown below.

$ virtualenv projenv`



Running the Application
You can also run the application using flask command.

Before running flask, set and export the environment variable FLASK_APP. The two steps are shown below.


(porjenv) $ export FLASK_APP=hello.py

(projenv) $ flask run

* Serving Flask app "hello" (lazy loading)

.....

.....

.....

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Activating a Virtual Environment
Regardless of the method, you select to create a virtual environment; the virtual environment needs to be activated before using it.

A newly created virtual environment can be activated using source command as shown below


$ source projenv/bin/activate

(projenv) $ _

You can exit the virtual environment simply by using deactivate command as shown below.

(projenv) $ deactivate

$ _


Managing Dependencies
Packages required for an application can be managed using pip.

The syntax for installing a package is shown below.


pip install <package_name>

Similarly, you can uninstall a package with below command.

pip uninstall <package_name>

You can also upgrade a package with below command

pip install --upgrade <package_name> 


3) Handling Web requests
Flask handles web requests through Routing.

Flask directs a web request to function, which is bind to the request URL using route decorator.

Then the bound function processes the request and returns an HTTP response to the user.

The route decorator takes one parameter named rule. The value passed to rule parameter represents the URL accessed by a user.


Variable Rules
Flask allows capturing different portions of a URL and pass them to the bound function, as parameters, for further processing.

For achieving this, the rule parameter value is allowed to contain variable parts, representing portions of accessed URL, which needs to be captured.

The variable part of a rule parameter value is identified by a name, and the variable name is embedded inside a pair of angle brackets.


Variable Part Converters
Any value captured by variable part of a rule parameter is a string.
Flask provides variable part converters, which can be used to convert default string value into another type.
Allowed converters are:
    int - Converts to an integer,

    float - Converts to a float, and

    path - Converts to a directory path, i.e. it accepts slashes that are used as directory path separator.




Redirecting a URL
Flask provides redirect functionality, which is used to redirect the browser's response to a specified URL.
redirect function takes a URL as the argument and calls the function associated with that URL, when redirect function is called.




Generating Dynamic URLs
Flask provides another functionality - url_for, which can be used for generating dynamic URL's.
url_for accepts a view function name as a mandatory argument and optional keyword arguments.
The below expressions show the usage of url_for.

    url_for('hello') returns the URL /

    url_for('hello_user', username='Michael') returns /user/Michael


Using Templats in Flask
Displaying HTML Pages


Creating Your First Template
In Flask, a template is a separate file present inside templates folder located in an application package.
For understanding, working with templates, let's create a folder named templates in helloapp folder.
Let's also convert helloapp folder into a package by creating an empty __init__.py in it as shown below.
(projenv) $ mkdir templates

(projenv) $ touch __init__.py

in index.html

Most of the content specified is simple html content, except the one enclosed in {{ ... }} portion.
These portions represent parts of a page, which are variable and occupies the values passed to the rendering template.

Conditionals in Templates
Templates in Flask also support the usage of conditional statements, mentioned in {% ... %} blocks.
            {% if user %}
        <h1>Hello {{user}}!!!</h1>
        {% else %}
        <h1>Hello World!!!</h1>
        {% endif %}

Loops in Templates
It is also possible to write loops inside templates.
You can write for loop inside {% ... %} blocks.



Need for Template Inheritance
As of now, the application contained two templates index.html and users.html.
Some portions of both these templates are same. For example the head portion and the HTML code displaying navigation bar.
When your application grows, you have to maintain several copies of these portions in many HTML templates.
Whenever you wanted to make changes to head or navigation bar portions, you have to edit many HTML templates.
Hence, it is not recommended to repeat the content.
This can be achieved with Template Inheritance feature of jinja2.


Template Inheritance
Template Inheritance feature allows writing parts of HTML page layout, which are common to many templates, in one template and derives other templates from it.
In this topic, you will create a template base.html, which holds common portions and also modify index.html and users.html such that they inherit contents of base.html.

block control statement is used to define a place holder, where derived templates can insert their specific content.
Each block is given a unique name, which is referenced inside derived templates.


Deriving Index Template
To inherit content from an existing template, extends template tag is used in the derived template.


https://stackoverflow.com/questions/61005805/need-help-in-code-for-writing-view-functions-in-flask-python-web-framework#:~:text=.choice(quotes)-,Define%20below%20a%20view%20function%20%27display_quotes%27%2C%20which%20returns%20an,%27%20header%20%22Famous%20Quotes%22.


Reorganizing the project
sampleproject/

   projenv/

      ....

   helloapp/

       templates/

          index.html

          users.html

       __init__.py

       hello.py

Application Initialization Settings
Most of the times an application initialization settings are done in __init__.py file, present in an app folder.
Hence, let's copy the below portion from hello.py and paste into __init__.py file, present in helloapp folder.
    from flask import Flask

    app = Flask(__name__)

Also, remove the above portion from hello.py file.


Application Views
Now let's keep all the application view functions in a single file.
For achieving that, remove the below-shown portion from hello.py file.
    if __name__ == '__main__':
    app.run()

Now let's also rename the file hello.py to routes.py using mv command as shown below.



Introduction to Extensions
Flask is a microframework that can be used only to build simpler applications.
Extra functionality can be added to an existing Flask application using an Extension
Extension is an extra package, which might add functionality such as sending an email or connecting to a database.
Few Extensions add entire new frameworks to build a certain type of applications such as REST API applications.


Finding Extensions
In general flask, extensions are named as Flask-Foo or Foo-Flask. Foo refers to an extension name.
Information about most of the flask extensions is available at http://flask.pocoo.org/extensions/.
Packages of flask extensions can also be searched at pypi.org.


Installing Extensions
Most easiest way of installing a flask extension is by using pip.

    pip install flask-sqlalchemy



Using Extensions
An example of using Flask-Foo extension is shown below.

    from flask-foo import Foo
    foo = Foo()
    app = Flask(__name__)
    foo.init_app(app)

