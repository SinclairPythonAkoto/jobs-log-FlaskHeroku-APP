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
* Changes to the app and including homepage.html works
* By setting {% extends "index.html" %} at the top of the homepage file, jinja accesses the data from index.html.
* The next step is to include a 'GET' & 'POST' method in the in the homepage route.

TP #6
* I need to create the database - so that means I need to create the schema and maybe test it by creating some test data to input.
* import os & psycopg2 and create a schema then test it.
* Change the code in the py file to include the py code from myfirst-flask-herokuAPP - but change it around slightly.
* Inititilize the database then push to heroku master

TP #7
* The inititilization of the database worked but the page did not run so I looking at other ways to connect to the database.
* Found another way through psycopg2, so I will make an attempt by using that.
* Firstly, try see if I can fix a bug with a correction of spelling..
* This didn't work; the page still failed to load.

TP #8
* I have put connection = pyscopg2.connect(....) inside the home route function; recorrect thi placing the connection in the global (place it out of the home function)
* Remove or delete the before_request function & connect_db function.
* I am testing if I can connect to the database through this way.
* Personally, I'm beginning to think that I need to put psycopg2.connect(os.environ.get('DATABASE_URL')) into a variable and see if I can connect to the database that way in the homepage route.
* If this doesn't work then seek other solutions.
* After watching a tutorial on YouTube (Uisning Python to query Postgres) I am startting to believe I have queried the postgres database all wrong! I think I will try the pyscopg2 method to connect to my database.
* This didnt work - need to find another solution.

TP #9
* Try create engine method to connect to my postgres (like in my other heroku walk-through)
* Use sqlalchemy & create engine to try connect to my page.
* This didn't work; try to fiund out if there are bug errors within my attempted solution or find a different solution.

TP #10 
* I found a way of connecting to your database through Flask & Flask-SQLAlchemey.
* I really want to avoid using stackoverflow.com so I will attempt to use the example I found.
* This uses a class to create your te mode of your database then create it in the python termina. 
* What I will do is follow some of the steps as the walk-through but not all as some files have already been created (procfile, wsgi etc)
* I have noticed that this walk-through uses a different database connection method
* I might need to test this on my local first...
* THINGS TO THINK ABOUT: What is the repr function? How will that be applied to my database class model? What are the new add ons and why do I need them?


<!-- TP #9
* I know I can create web pages (without a database) and make it run through Heroku
* Now I just need to find a way to connect to my postgres through Heroku
* I know it can be done because I have done it before in other walkthroughs I have completed.
* Keep reviewing tutorials & documentation along with trail & error when testing the page.
* Upload my code to stackoverflow.com to find a solution if I still get stuck. -->