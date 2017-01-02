from flask import Flask, render_template, request, flash, redirect
from flask_heroku import Heroku
from forms import SubmitForm
import sqlite3
app = Flask(__name__)
app.config.from_object("config.TestingConfig")
heroku = Heroku(app)


@app.route('/')
def home_page():
    return render_template("./index.html", title="Home")


# @app.route('/submit_score', methods=['GET', 'POST'])
def submit_score(username, score):
    try:
        conn = sqlite3.connect('pong.db')
        c = conn.cursor()
        c.execute("INSERT INTO leaderboard "
              "values (?, ?)", (username, score))

        conn.commit()
        conn.close()
        return True
    except:
        return False


@app.route('/game', methods=['GET', 'POST'])
def game_page():

    form = SubmitForm()
    if form.validate_on_submit():
        submitted = submit_score(request.form["username"], request.form["score"])

        # if value submits to database, redirect to leaderboard and highlight row added
        if submitted:
            conn = sqlite3.connect('pong.db')
            c = conn.cursor()
            l = [val for val in c.execute("SELECT * FROM leaderboard ORDER BY score DESC")]
            return render_template("leader_board.html", title="Leader Board", leaderboard=l,
                            highlight=request.form["username"])

        else:
            flash("submission failed")

    return render_template("game.html", title="Game", win_point=1, form=form)


@app.route('/leader_board')
def leader_board():
    conn = sqlite3.connect('pong.db')
    c = conn.cursor()
    l = [val for val in c.execute("SELECT * FROM leaderboard ORDER BY score DESC")]
    return render_template("leader_board.html", title="Leader Board", leaderboard=l, highlight="")

if __name__ == "__main__":
    app.run()