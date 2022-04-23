from flask import render_template
from core import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", pages=app.context)


@app.route("/pages/<page>")
def page(page):
    name = page.split(".")[0].replace("_", " ").split(" ")[1:]
    name = " ".join(name)

    return render_template("pages/" + page, name=name)
