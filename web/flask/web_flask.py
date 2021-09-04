from flask import Flask

# from flask import g
from flask import render_template

from flask import request

# from flask import Response

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/goodnight")
@app.route("/goodnight/<name>")
def good_night(name=None):
    return f"good night {name}"


@app.route("/name")
@app.route("/name/<name>")
def say_name(name=None):
    return render_template("hello.html", name=name)


@app.route("/get_test", methods=["get"])
def post_sample():
    # return request.query_string
    return request.values["name"]


def main():
    app.debug = True
    # app.run(host="127.0.0.1", port=5000)
    app.run()


if __name__ == "__main__":
    main()
