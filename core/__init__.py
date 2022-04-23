import os
from flask import Flask


def get_context():
    context = []
    for file in os.listdir("templates/pages"):
        if file.endswith(".html"):
            title = file.split(".")[0].replace("_", " ")
            name = title.split(" ")[1:]
            name = " ".join(name)
            name = name.upper()
            rollNo = title.split(" ")[0]
            url = "pages/" + file
            context.append({"name": name, "rollNo": rollNo, "url": url})
    return context


app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.context = get_context()

from core import urls
