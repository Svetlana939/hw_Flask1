from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/fantastic')
def fantastic():
    return render_template("fantastic.html")


@app.route('/classic')
def classic():
    return render_template("classic.html")


@app.route('/whodunit')
def whodunit():
    return render_template("whodunit.html")


if __name__ == "__main__":
    app.run(debug=True)