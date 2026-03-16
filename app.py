from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# temporary user storage
users = {}


# first page → login
@app.route("/")
def start():
    return redirect("/login")


# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email] == password:
            return redirect("/planner")

        else:
            return "Invalid Login"

    return render_template("login.html")


# SIGNUP
@app.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        users[email] = password

        return redirect("/login")

    return render_template("signup.html")


# SMART STUDY PLANNER (your existing logic)
@app.route("/planner", methods=["GET","POST"])
def planner():

    if request.method == "POST":

        subject = request.form["subject"]
        exam_date = request.form["date"]
        difficulty = request.form["difficulty"]

        today = datetime.today()
        exam = datetime.strptime(exam_date, "%Y-%m-%d")

        days_left = (exam - today).days

        topics = ["Unit 1","Unit 2","Unit 3","Unit 4","Revision","Mock Test"]

        plan = []

        for i in range(min(days_left, len(topics))):
            plan.append(f"Day {i+1}: Study {topics[i]}")

        plan = "<br>".join(plan)

        return render_template("index.html", plan=plan)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)