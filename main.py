
#imports
import requests


#froms
from  flask import Flask, jsonify, request, render_template, Response

app = Flask(__name__)


@app.route('/')
def home():
	Teams_URL = "https://statsapi.web.nhl.com/api/v1/teams"
	r = requests.get(Teams_URL)
	r = r.json()
	return render_template("home.html")

@app.route('/team/<ID>')
def teams(ID):
	One_Team_URL = ("https://statsapi.web.nhl.com/api/v1/teams/"+ID+"?expand=team.stats")
	r = requests.get(One_Team_URL)
	r = r.json()
	team_data = r["teams"][0]
	team_stats = team_data["teamStats"][0]
	team_splits = team_stats["splits"][0]
	final_stats = team_splits["stat"]
	team_api_info = team_splits["team"]
	final_team_name = team_api_info["name"]
	final_stats["team"] = final_team_name
	
	return f"The stats of the {final_team_name} are: {final_stats}"


if __name__ == "__main__":
	app.run(debug=True)

