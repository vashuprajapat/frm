# flask app to handle form and send data to google sheets

from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, jsonify, request, abort,redirect

import os
app = Flask(__name__)

credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)

gsheet = client.open("Police info").sheet1
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_review', methods=["GET", "POST"])
# def add_review():
#     if request.method == "POST":
#         data = request.get_json()
#         print(data+"getjson")
#         gsheet.append_row(list(data.values()))
#         return redirect("https://viveks-codes.github.io/Pratipushti/vishal/thankyou.html", code=302)
#     elif request.method == "GET":
#         data = request.args
#         print(data)
#         gsheet.append_row(list(data.values()))
#         return render_template('index.html')
#         return jsonify({"success": False, "error": "Invalid request method"})

@app.route('/add_review', methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        # take data where name is "q1", "q2", message
        data = request.form.to_dict()
        # append data to google sheet
        gsheet.append_row(list(data.values()))
        print(data)
        return redirect("https://viveks-codes.github.io/Pratipushti/hunaid/enddd.html", code=302)
    elif request.method == "GET":
        data = request.args
        print(data)
        gsheet.append_row(list(data.values()))
        return render_template('index.html')
        return jsonify({"success": False, "error": "Invalid request method"})

# @app.route('/update_review', methods=["PATCH"])
# def update_review():
#     req = request.get_json()
#     cells = gsheet.findall(req["  "])
#     for c in cells:
#         gsheet.update_cell(c.row, 3, req["score"])
#     return jsonify(gsheet.get_all_records())
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))

# http://192.168.200.186/add_review?District=Surat&Taluka=mahuva&District=anawal&subdiv=Sub%20div-1&Polics-station=police%20chawki-3surat&How%20did%20you%20come%20to%20police%20station?=idontknow&After%20how%20much%20time%20you%20were%20heard%20in%20police%20station?=i%20dkkkkkk&Describe%20your%20expiriance%20with%20police%20in%20police%20station=idkif%20this%20works&
