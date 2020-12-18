import csv
import os
from main import csv_creator
from flask import Flask, render_template, redirect, url_for
from src.cmd_user_interface import CmdUserInterface

app = Flask(__name__)

# The default homepage for the app
@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/posts')
def headers():
    # If there is a pre-existing csv file this will remove it
    # This is to ensure the app always uses the newest data present
    if os.path.exists("~/Downloads/ItJobsWatchTop30.csv"):
        os.remove("~/Downloads/ItJobsWatchTop30.csv")
    # This comes from the main.py file, it will insert a csv of the data in ~/Downloads
    csv_creator(1)
    jobs_list = {}
    with open("/home/ubuntu/Downloads/ItJobsWatchTop30.csv", newline="") as jobs:
        reader = csv.reader(jobs)
        i = 0
    # Each line in the csv is inserted into the dictionary as a value
    # The key for each line being the integer `i`
        for job in reader:
            if job == [ ]:
                continue
            jobs_list[int(f"{i}")] = job
            i += 1
    # I return the template with the dictionary as a variable to substitute into the HTML
    return render_template("with-headers.html", job=jobs_list)


@app.route('/fibonacci')
def no_headers():
    # If there is a pre-existing csv file this will remove it
    # This is to ensure the app always uses the newest data present
    if os.path.exists("~/Downloads/ItJobsWatchTop30.csv"):
        os.remove("~/Downloads/ItJobsWatchTop30.csv")
    # This comes from the main.py file, it will insert a csv of the data in ~/Downloads    
    csv_creator(1)
    jobs_list = {}
    with open("/home/ubuntu/Downloads/ItJobsWatchTop30.csv", newline="") as jobs:
        reader = csv.reader(jobs)
        i = 0
    # Each line in the csv is inserted into the dictionary as a value
    # The key for each line being the integer `i`
        for job in reader:
            if job == [ ]:
                continue
            jobs_list[int(f"{i}")] = job
            i += 1
    # I return the template with the dictionary as a variable to substitute into the HTML
    return render_template("without-headers.html", job=jobs_list)


# A simple error page
@app.route('/error')
def error():
    return render_template("error.html")


# A 404 error will redirect someone to the error page above
@app.errorhandler(404)
def not_found(Exception):
    return redirect("/error")


if __name__ == "__main__":
    app.run()
    