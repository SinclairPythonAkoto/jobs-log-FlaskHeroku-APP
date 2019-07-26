import os
import psycopg2
import psycopg2 as p
from flask import Flask, render_template, request, redirect, url_for, g
from time import gmtime, strftime


app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


# def connect_db():
#     return psycopg2.connect(os.environ.get('DATABASE_URL'))
 

# @app.before_request
# def before_request():
#     g.db_conn = connect_db()

# con = p.connect("dbname='dfejjkn0m6m8hn' user='postgres' host='ec2-174-129-226-234.compute-1.amazonaws.com'")
# db = con.cursor()



@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		# db.execute("SELECT * FROM LogTable")
		# entry = db.fetchall()
		return render_template("homepage.html")#, entry=entry)
	else:
		date_entry = request.form.get("job_date") # Date in LogTable
        time_entry = request.form.get("job_time") # Time in LogTable
        job = request.form.get("job_options") # Job in LogTable
        description = request.form.get("description") # Description in LogTable
        outcome = request.form.get("job_outcome") # Outcome in LogTable
        comments = request.form.get("additional_comments") # Comments in LogTable
        date_stamp = strftime("%d-%m-%y", gmtime()) # Date_Entry in LogTable
        time_stamp = strftime("%H:%M", gmtime()) # Time_Entry in LogTable
        
        # db.execute("INSERT INTO LogTable (Date_Entry, Time_Entry, Job, Description, Outcome, Comments, Date_Stamp, Time_Stamp VALUES (:date_entry,:time_entry,:job,:description,:outcome,:comments,:date_stamp,time_stamp)", {"Date_Entry":date_entry, "Time_Entry":time_entry, "Job":job, "Description":description, "Outcome":outcome, "Comments":comments, "Date_Stamp":date_stamp, "Time_Stamp":time_stamp})
        # db.commit()
        
        return redirect(url_for("home"))


if __name__ == '__main__': app.run(debug=True)