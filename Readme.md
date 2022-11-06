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



Introduction to Databases
Flask, by default, doesn't provide any support for connecting to any database.
Hence Application developers are free to choose any database and integrate it with their application
A large number of databases are available in market, and many of them possess Python APIs.
These databases can mainly be grouped into Relational and NoSQL databases.
Relational databases store Structured data and NoSQL databases store Unstructured data.

Connecting to Databases
Database specific Flask extensions are available for connecting to various databases such as Flask-MySQL - an extension for MySQL
On the other hand, SQLAlchemy can connect to many relational databases.
SQLAlchemy is an Object Relational Mapper (ORM), which allows connecting to databases in an object-oriented way rather than using SQL queries.
It converts the method calls into database commands and execute them.
Flask-SQLAlchemy extension is a wrapper for SQLAlchemy. It can be installed using pip as shown below.
    pip install flask-sqlalchemy


FLASK-SQLAlchemy Configuration
In this course, you will work with an SQLite database, hello.db.
SQLite databases are light one's and don't require any separate database server like MySQL, and PostgreSQL.
You need to tell the application, where it can find the database.
In order to achieve it, let's create a configuration file config.py inside helloapp folder and add the below content.

The Flask-SQLAlchemy extension understands the application database location from SQLALCHEMY_DATABASE_URI configuration variable.
From config.py you can observe that SQLALCHEMY_DATABASE_URI value is set to value of environment variable DATABASE_URL.
If DATABASE_URL value is not defined, then SQLALCHEMY_DATABASE_URI value is set to hello.db database located in sampleproject folder.
The variable SQLALCHEMY_TRACK_MODIFICATIONS is a setting which allows tracking of modifications done to database. Currently it is set to False.

Now modify helloapp/__init__.py file as shown below. It imports Config class defined in config.py, sets configurations of the application, and also creates a database instance.



Introduction to Database Models
Every table in a database is represented by a class, usually known as a database model.
Also, each object of a database model class represents a row of the corresponding table.
Hence, a database is a collection of classes.
The ORM layer of SQLAlchemy performs all the translations required for mapping database model class objects into rows of the corresponding table.





Database Migrations
In order to propagate the model class definition into the database schema, you need to perform a Database Migration.
This can be achieved using Flask-Migrate extension. It is a wrapper for Alembic - a database migration framework for SQLAlchemy.
You can install Flask-Migrate extension using pip as shown below.
    pip install flask-migrate
This extension also helps in updating changes done to the existing database in future.
After installing Flask-Migrate extension, create a Migration instance by adding the below lines to helloapp/__init__.py


Creating a Migration Repository
Alembic maintains a migration repository that stores the application migration scripts
Whenever a change is done to a database schema, a new migration script is created and added to the repository.
To reflect the changes in the database, the migration scripts are executed in the sequence they were created.
You can now create a migration repository using flask db init command as shown below.



Generating Database Migration Script
Once the migration repository is created, Now let's perform the first migration using flask db migrate command shown below.
It creates a migration script 4c1a9e3a41e0_creating_user_table.py in migrations/versions folder.
It doesn't make any changes to the database.


Applying Changes to Database
The migration script created using flask db migrate command contains two function definitions: upgrade and downgrade.
To apply the changes to a database, you have to run the command flask db upgrade as shown below



Inserting Data into Database
First of all, let's start a python shell using flask shell command as shown below.
Now let's create two user objects using below code.

    >>> from helloapp.models import User

    >>> user1 = User(fname="James", lname="smith", email="james@abc.com")

    >>> user2 = User(fname="Sam", lname="Billings", email="sam@xyz.com")


Finally let's save the changes with below statements. Only db.session.commit() will write the changes to database.

    >>> from helloapp import db

    >>> db.session.add(user1)

    >>> db.session.add(user2)

    >>> db.session.commit()


Querying a Database
Now let's see how to query a table and fetch the records.

In Flask all models have a query attribute, which can be used to run database queries.

Consider the below-shown expressions. The first one fetches all records from the table user, and the second one filters only those records whose fname field has the value James.

    >>> User.query.all()

    [<User : James smith>, <User : Sam Billings>]

    >>> User.query.filter(User.fname == 'James').all()

    [<User : James smith>]



Working with Web forms
Introduction to Flask-WTF

Web Forms are the basic building blocks of a Web Application.
Web Forms are specifically used to accept input from users.

Flask-WTF extension handles web forms. It is a wrapper around WTForms package and nicely integrates WTForms with Flask.

Flask-WTF extension can be installed using pip as shown below.
    pip install flask-wtf


Flask-WTF Configuration
Once Flask-WTF is installed successfully, SECRET_KEY configuration variable has to be set.
So let's define a class variable SECRET_KEY in class Config of config.py file as shown below.

The value of SECRET_KEY is set to value of environment variable with the same name. If that value is not defined, then it is set to a hard-coded string value.

Flask and some of its extensions use SECRET_KEY value for generating signatures and tokens.

Flask-WTF uses SECRET_KEY value to protect web forms against Cross-Site Request Forgery (CSRF).



Defining User Form
Flask-WTF uses classes to represent a web form. The fields of the form are defined as class variables.
Now let's create a form named UserForm in helloapp/forms.py file, as shown below




Writing a Template
Now let's create a new template adduser.html, which renders UserForm to a user.

All the fields defined in UserForm are rendered as HTML.

The adduser.html template

You can observe that the template adduser.html is derived from base.html.

The template also expects an object of UserForm class to be passed as an argument. The argument is passed in a view function, which renders adduser.html template.

The form.csrf_token template argument is required to protect the form against CSRF attacks.

To include a field label, in the template, use the expression of the form {{ form.<field_name>.label }}. It is rendered as HTML.

Similarly to include a field, use the expression of the form {{ form.<field_name> }}.




Writing a View Function
After defining the form template, now let's define the view function useradd to helloapp/routes.py, as shown below.




Receiving Form Data
Now try providing some data into the displayed form and click on submit button.

It throws Method Not Allowed error to the user.

This is because the defined adduser function doesn't have any logic to process data submitted by a user.

Now let's modify useradd view function as suggested below.



    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField, validators
    #from wtforms.validators import DataRequired, Length, Email
    class UserForm(FlaskForm):
    fname = StringField("First Name",  [validators.DataRequired(), validators.Length(min=3, max=100)])
    lname = StringField("Last Name", [validators.DataRequired(), validators.Length(min=3, max=100)])
    email = StringField("Email", [validators.DataRequired(), validators.Email("Please provide a valid email address.")])
    submit = SubmitField("Submit")