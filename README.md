This is my first attempt at creating a jobs log app using Python, Flask, PostgreSQL & Heroku.

 I have used a Flask-Heroku template provided by https://github.com/Vetronus/heroku-flask-template.

Test the app: https://sinclair-python-akoto-jobs-log.herokuapp.com

STEPS I MADE

1. Create folder 'HEROKU APPS' in my desktop.

2. Navigate to the 'HEROKU APPS' folder in your file directory, and open in Bash.

3. Create new pository in GitHub and then clone it in Bash.  When cloning, add && cd FOLDER-NAME at the end of the git clone .... This is where your files will be added into.

4. I have downloaded the zip file from https://github.com/Vetronus/heroku-flask-template.  From the zip file copy and paste files into FOLDER-NAME inside the HEROKU APPS folder.

5. Make adjustments to the README file and (I done this first to avoid confusion).  After the adjustments made:
'git add .' (adds adjusted file) | 
'git commit -m "COMMIT COMMENT"' (commits your changes) |
'git push' (saves your changes to your repository on GitHub)

6. Open a seperate Bash window; log into Heroku by typing 'heoku login'.  A new HTML window will pop up and once you click the button you should be  logged in inside Bash.

7. Now in your orginal Bash window, create a new Heroku App by 'heroku create HEROKU-APP-NAME'.  You will recieve a Herokuapp https & your GitHub repository (the original).  You can always check on your remote by 'git remote -v'.  This will also show you your Heroku & Git connection.  You can also check your Heroku dasboard and should see your new app.

8. 'git push heroku master' to save your heroku app and any changes made.

9. Now set your Python path by: 'heroku config:set PYTHONPATH='
I have left that empty because you should really keep it a secret.


TIPS

* If you need to reconnect your git to your heroku app just type 'heroku git:remote -a HEROKU-APP-NAME'
* 'heroku apps' will give you a list of your heroku apps in Bash