import csv
import os
from main import csv_creator
from flask import Flask, render_template, redirect
from src.cmd_user_interface import CmdUserInterface

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/posts')
def headers():
    if os.path.exists("~/Downloads/ItJobsWatchTop30.csv"):
        os.remove("~/Downloads/ItJobsWatchTop30.csv")
    csv_creator(1)
    jobs_list = {}
    with open("/home/ubuntu/Downloads/ItJobsWatchTop30.csv", newline="") as jobs:
        reader = csv.reader(jobs)
        i = 0
        for job in reader:
            if job == [ ]:
                continue
            jobs_list[int(f"{i}")] = job
            i += 1
    return render_template("with-headers.html", job=jobs_list)


@app.route('/fibonacci')
def no_headers():
    if os.path.exists("~/Downloads/ItJobsWatchTop30.csv"):
        os.remove("~/Downloads/ItJobsWatchTop30.csv")
    csv_creator(1)
    jobs_list = {}
    with open("/home/ubuntu/Downloads/ItJobsWatchTop30.csv", newline="") as jobs:
        reader = csv.reader(jobs)
        i = 0
        for job in reader:
            if job == [ ]:
                continue
            jobs_list[int(f"{i}")] = job
            i += 1
    return render_template("without-headers.html", job=jobs_list)


@app.route('/error')
def error():
    return render_template("error.html")

@app.errorhandler(404)
def not_found(Exception):
    return redirect("/error"), 404


if __name__ == "__main__":
    app.run()
    