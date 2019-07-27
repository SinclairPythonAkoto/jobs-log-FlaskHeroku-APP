import os
import psycopg2

from flask import Flask, render_template, request, redirect, url_for, g
from time import gmtime, strftime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

@app.before_request
def before_request():
    g.db_conn = connect_db()

 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dwsucfpgbapscm:ab6db8b3d1a814ba8fd31acf9b9235191b8ef4dffc658317f326cd80bfb4f514@ec2-174-129-209-212.compute-1.amazonaws.com:5432/d7p546rpkautd7'
# db = SQLAlchemy(app) 

# engine = create_engine("postgres://postgres:161086@ec2-174-129-226-234.compute-1.amazonaws.com:5432/dfejjkn0m6m8hn")
# db = scoped_session(sessionmaker(bind=engine))


# @app.before_request
# def before_request():
#     g.db_conn = connect_db()

# con = p.connect("dbname='dfejjkn0m6m8hn' user='postgres' host='ec2-174-129-226-234.compute-1.amazonaws.com'")
# db = con.cursor()



@app.route('/', methods=['GET', 'POST'])
def home():
	# if request.method == 'GET':
	# 	cur = g.db_conn.cursor()
	# 	entry = cur.execute("SELECT * FROM LogTable;").fetchall()
	# 	return render_template("homepage.html", entry=entry)
	# else:
	# 	date_entry = request.form.get("job_date") # Date in LogTable
	# 	time_entry = request.form.get("job_time") # Time in LogTable
 #        job = request.form.get("job_options") # Job in LogTable
 #        description = request.form.get("description") # Description in LogTable
 #        outcome = request.form.get("job_outcome") # Outcome in LogTable
 #        comments = request.form.get("additional_comments") # Comments in LogTable
 #        date_stamp = strftime("%d-%m-%y", gmtime()) # Date_Entry in LogTable
 #        time_stamp = strftime("%H:%M", gmtime()) # Time_Entry in LogTable
        
 #        cur.execute("INSERT INTO LogTable (Date_Entry, Time_Entry, Job, Description, Outcome, Comments, Date_Stamp, Time_Stamp VALUES (:date_entry,:time_entry,:job,:description,:outcome,:comments,:date_stamp,time_stamp)", {"Date_Entry":date_entry, "Time_Entry":time_entry, "Job":job, "Description":description, "Outcome":outcome, "Comments":comments, "Date_Stamp":date_stamp, "Time_Stamp":time_stamp})
 #        cur.commit()
        
 #        return redirect(url_for("home"))
    cur = g.db_conn.cursor()
    entry = cur.execute("SELECT * FROM LogTable;").fetchall()
    return render_template('homepage.html')


if __name__ == '__main__': app.run(debug=True)

