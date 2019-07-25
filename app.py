from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
	hello = "Hello World!"
    return render_template("index.html", hello=hello)





if __name__ == '__main__': app.run(debug=True)