from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    dt_now = datetime.datetime.now()
    now = dt_now.strftime('%Y/%m/%d %H:%M:%S')
    return render_template("index.html",now = now)


if __name__ == "__main__":
    app.run(debug = True)
