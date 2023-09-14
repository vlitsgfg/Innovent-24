from flask import Flask, render_template, request, redirect
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

from datetime import datetime
import json
import os

ATTENDANCE_FILE_NAME = "emp-attendance.json"
EMPLOYEE_LIST_FILE_NAME = "emp-list.json"
DATE_FORMAT = "%d-%m-%Y"
CUTOFF_HOUR = 18

loggedin_users = set()

app = Flask(__name__)
app.config.update(
	TEMPLATES_AUTO_RELOAD=True
)

def save_attendance(empID):
	print("Saving attendance for", empID)
	current_attendance = {}
	try:
		with open(ATTENDANCE_FILE_NAME, "r+") as f:
			current_attendance = json.load(f)
	except:
		pass

	today = datetime.today().strftime(DATE_FORMAT)
	if today in current_attendance:
		current_attendance[today].append(empID)
		current_attendance[today] = list(set(current_attendance[today]))
	else:
		current_attendance[today] = [empID]

	with open(ATTENDANCE_FILE_NAME, "w+") as f:
		json.dump(current_attendance, f, indent=4)


@app.route("/")
def index_page():
	return render_template("index.html")


@app.route("/emp", methods=["GET", "POST"])
def emp_index_page():
	if request.method == "GET":
		return render_template("emp-login.html")
	else:
		request.form["username"]


@app.route("/emp/scan")
def emp_scan_page():
	if (request.args.get("password") == "999"):
		return render_template("emp-scan.html", CUTOFF_HOUR=CUTOFF_HOUR)
	else:
		return redirect("/emp")


@app.route("/emp/submit", methods=["GET", "POST"])
def emp_submit_endpoint():
	time_now = datetime.now().time()
	# breakpoint()
	if time_now.hour >= CUTOFF_HOUR:
		return "Time over"

	file = request.files["file"]

	data = decode(Image.open(file.stream))
	if len(data) > 0:
		data = data[0].data.decode()
		print(data)
		save_attendance(data)
		return data
	else:
		return "No data found"


@app.route("/emp/get_attendance")
def calcluate_attendance():
	empID = request.args.get("id")

	if empID is None:
		return render_template("emp-get_attendance.html", perc="")

	attendance = None
	with open(ATTENDANCE_FILE_NAME) as f:
		attendance = json.load(f)

	emp_list = None
	with open(EMPLOYEE_LIST_FILE_NAME) as f:
		emp_list = json.load(f)

	if empID not in emp_list:
		return render_template("emp-get_attendance.html", perc="Not found")

	number_of_days = len(attendance)

	if number_of_days < 0:
		return render_template("emp-get_attendance.html", perc="No attendance recorded")


	# breakpoint()
	count = 0
	for date, emps in attendance.items():
		if empID in emps:
			count += 1

	perc = round(count * 100 / number_of_days, 2)
	perc = empID + ": " + str(perc) + "%"

	return render_template("emp-get_attendance.html", perc=perc)


@app.after_request
def add_header(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers["Cache-Control"] = "public, max-age=0"
	return r


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
