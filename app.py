import os
from flask import Flask
from flask import render_template,jsonify,request, redirect,url_for
import csv
import sys
import server
from server import *
import sys
import json
from JSONEncoder import JSONEncoder
from login import *
import json, xmltodict

app = Flask(__name__)

db = server.get_db()

username = None
mygames={}

maincollection = None

reload(sys)
sys.setdefaultencoding('utf-8')

def logged_in():
	if username is not None:
		return 1
	else:
		return 0


@app.route("/")
def home():
	return render_template('login.html')

@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
	print request.json["username"]
	if open_account(request.json["username"]):
		print "logged in"
		return main()
	else:
		print "not logged in" 
		return None

@app.route("/home")
def main():
	if logged_in():
		return render_template('index.html')
	else:
		return home()




	#return render_template('index3.html', games = mygames)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)