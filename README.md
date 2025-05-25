# **Web Services and Applications**

## **Task Manager App**

<img src="https://realpython.com/cdn-cgi/image/width=640,format=auto/https://files.realpython.com/media/UPDATE-Python-Web-Applications-with-Flask-1_Watermarked.3e384f2e53cf.jpg">



### **PROJECT OVERVIEW:** 

Task Manager is a web application built using Flask(Python), HTML/CSS, MySQL and jQuery. It allows users to view all tasks, create new tasks, edit and delete tasks through a web interface. 

Hosted at: https://louiser.pythonanywhere.com/


### **HOW IT WORKS:**

-   Users interact with the webpage to view, add, delete or update tasks. 
-   This causes JavaScript functions to execute, which use AJAX to send HTTP requests to the Flask server without reloading the page
    -   GET requests: get all tasks
    -   POST requests: add new task
    -   PUT requests: update task
    -   DELETE requests: delete task
-   The flask server handles the requests by calling methods in TasksDAO class to interact with the MYSQL database. 
-   JavaScript updates the web page dynamically based on the server response 



### **SETUP:**

*Clone the repository:*

-   ```git clone https://github.com/lryan30/wsaa_project```

*Set up virtual environment and install dependencies:*

-   ```python -m venv venv```
-   ```venv/bin/activate```
-   ```pip install -r requirements.txt```

*Run the application locally:*

-   run *python appserver.py* on command line.

-   Open webbrowser at http://127.0.0.1:5000/

*Hosting the application on PythonAnywhere.com:*


-   upload project files
-   create database via MySQL console on PythonAnywhere
-   set up virtual environment and install dependencies there


### **FILE STRUCTURE:**

-   **index.html:** Front-end webpage where users interact with the Task Manager. It contains the HTML, CSS and Javascript with AJAX for viewing, creating, updating and deleting tasks. 

-   **appserver.py:** Flask application server with RESTAPI endpoints and handles the HTTP requests from the front end. It uses the taskDAO.py methods to interact with the database and return JSON responses. 

-   **dbconfig.py:** Contains the database connection settings such as host, user, password, and database name. This file is imported by taskDAO.py to establish a connection with the MySQL database.
-   **taskDAO.py:** Data Access Object (DAO) responsible for all database operations related to tasks. It provides methods to get, create, update, and delete tasks in the MySQL database.

-  **requirements.txt:** Lists all Python dependencies needed to run the project.


### **REFERENCES:**

-   [PythonAnywhere Guide] https://github.com/andrewbeattycourseware/deploytopythonanywhere
-   [Flask Documentation] https://flask.palletsprojects.com/en/latest/
-   [MySQL-Connector Documentation] https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
-   [Ajax-Intro W3Schools] https://www.w3schools.com/xml/ajax_intro.asp
-   [Python Requests]  https://realpython.com/python-requests/
-   [HTML Tutorial W3Schools] https://www.w3schools.com/html/
-   [JavaScript Tutorial W3Schools] https://www.w3schools.com/js/DEFAULT.asp
-   Chatgpt: generated sample data for MySQL database. gave guidance on Javascript AJAX integration and frontend logic. 
-   Image: https://realpython.com/flask-project/





