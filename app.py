import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///task.db")

@app.route("/")
def index():
    # get all the task from database
    tasks = db.execute("SELECT * FROM task")
    # return them
    return render_template("index.html", tasks=tasks)


@app.route("/new", methods=["POST", "GET"])
def new():
    if request.method == "POST":
        try:
            task = request.form.get("task")

            label = request.form.get("label")

        except ValueError:
            redirect("/")

        db.execute("INSERT INTO task (task, label) VALUES(?, ?)", task, label)

        return redirect("/")
    else:
        return render_template("new.html")


@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM task WHERE id = ?", id)
    return redirect("/")
