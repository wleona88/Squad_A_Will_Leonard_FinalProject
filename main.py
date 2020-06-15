
#imports
import requests


#froms
from  flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def home():
	Teams_URL = "https://statsapi.web.nhl.com/api/v1/teams"
	r = requests.get(Teams_URL)
	return r.json()

@app.route('/team/<ID>')
def teams(ID):
	One_Team_URL = ("https://statsapi.web.nhl.com/api/v1/teams/"+ID)
	r = requests.get(One_Team_URL)
	return r.json()

if __name__ == "__main__":
	app.run(debug=True)

