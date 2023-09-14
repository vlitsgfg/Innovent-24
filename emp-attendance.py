from flask import Flask, render_template, request
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

from datetime import datetime
import json
import os

ATTENDANCE_FILE_NAME = "emp-attendance.json"
DATE_FORMAT = "%d-%m-%Y"
CUTOFF_HOUR = 12

app = Flask(__name__)

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
		json.dump(current_attendance, f)

@app.route("/")
def index_page():
	return render_template("index.html", CUTOFF_HOUR=CUTOFF_HOUR)

@app.route("/submit", methods=["GET", "POST"])
def submit_endpoint():
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


@app.route("/get_attendance")
def calcluate_attendance():
	attendance = None
	with open(ATTENDANCE_FILE_NAME) as f:
		attendance = json.load(f)

	number_of_days = len(attendance)
	if number_of_days < 0:
		return "None"
	else:
		empID = request.args.get("id")
		count = 0
		for date, emps in attendance.items():
			if empID in emps:
				count += 1
		perc = round(count * 100 / number_of_days, 2)
		return empID + ": " + str(perc) + "%"


@app.after_request
def add_header(r):
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers["Cache-Control"] = "public, max-age=0"
	return r

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
