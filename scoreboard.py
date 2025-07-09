from flask import Flask, render_template
from datetime import datetime

scoreboard = Flask(__name__)

games = [
    {"team1" : "LG", "team2" : "삼성", "score" : "5 - 3", "status" : "종료"},
    {"team1" : "SSG", "team2" : "KT", "score" : "2 - 6", "status" : "9회초"},
    {"team1" : "KIA", "team2" : "한화", "score" : "4 - 1", "status" : "7회말"},
    {"team1" : "NC", "team2" : "롯데", "score" : "0 - 0", "status" : "8회말"},
    {"team1" : "두산", "team2" : "키움", "score" : "7 - 2", "status" : "종료"}
]

rankings = [
    {"team" : "LG", "wins" : "45", "losses" : "25", "pct" : "0.643"},
    {"team" : "SSG", "wins" : "42", "losses" : "28", "pct" : "0.600"},
    {"team" : "삼성", "wins" : "39", "losses" : "31", "pct" : "0.557"},
    {"team" : "두산", "wins" : "37", "losses" : "34", "pct" : "0.521"},
    {"team" : "키움", "wins" : "35", "losses" : "36", "pct" : "0.493"},
    {"team" : "KIA", "wins" : "34", "losses" : "36", "pct" : "0.486"},
    {"team" : "한화", "wins" : "33", "losses" : "37", "pct" : "0.471"},
    {"team" : "NC", "wins" : "32", "losses" : "38", "pct" : "0.457"},
    {"team" : "롯데", "wins" : "30", "losses" : "40", "pct" : "0.429"},
    {"team" : "KT", "wins" : "28", "losses" : "42", "pct" : "0.400"}
]

@scoreboard.route("/games")
def show_games():
    now = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    return render_template("games.html", games=games, now=now)

@scoreboard.route("/rankings")
def show_rankings():
    return render_template("rankings.html", rankings=rankings)

if __name__ == "__main__":
    scoreboard.run(debug=True)