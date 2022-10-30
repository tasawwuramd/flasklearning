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


