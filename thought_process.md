THOUGHT PROCESS DOCUMENTATION

After successfully loading the Flask Heroku template onto my repository, I changed some of the data in app.py & the contemt of the templates folder.

The documentation of my thought process is available below; from start to completion of jobs log web app.

TP #1
* Delete old files and change python file
* In the python file import os & psycopg2
* Write the same code as I did for the walk-through Heroku app I completed.

TP #2
* The above didn't work, so delete the files and start with basic 'Hello World' route to test if it works.
* This worked!

TP #3
* Now I will test index.html page to see if it works.
* I will change the return to render_template(); also make 'Hello World!' a string and store it in a variable.
* Use Jinja to inact code - testing if it works.
* Don't forget to put the html page & variable=variable into the render_template() !

TP #4
* That didn't work :(
* I don't understand why my jinja isn't working, what I will do is test the html page itself.
* If that works then test jinja with the "extends" page when I create the homepage.
* This works!

TP #5
* Create a homepage and use jinja as I would in my orginal jobs log app.