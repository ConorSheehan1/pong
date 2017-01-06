from flask import Flask, render_template, request, flash, redirect
from flask_heroku import Heroku
from forms import SubmitForm
import sqlite3
app = Flask(__name__)
app.config.from_object("config.Test")
# app.config.from_object("config.Production")
heroku = Heroku(app)


@app.route('/')
def home_page():
    return render_template("./index.html", title="Home")


def submit_score(username, score):
    '''
    no need for an app route, this method should just push to db and return boolean if it worked
    '''
    try:
        conn = sqlite3.connect('pong.db')
        c = conn.cursor()
        c.execute("INSERT INTO leaderboard values (?, ?)", (username, score))
        conn.commit()
        conn.close()
        return True
    except:
        return False


@app.route('/game', methods=['GET', 'POST'])
def game_page():

    # count number of players in database and just assign that number +1 to default anon name
    conn = sqlite3.connect('pong.db')
    c = conn.cursor()
    anon = [val for val in c.execute("SELECT COUNT(*) FROM leaderboard")][0][0]
    anon = "anon" + str(anon)

    form = SubmitForm()
    if form.validate_on_submit():
        print(form.errors)
        submitted = submit_score(request.form["username"], request.form["score"])
        print("submitted", submitted)

        # if value submits successfully to database, redirect to leaderboard and highlight row added
        if submitted:
            conn = sqlite3.connect('pong.db')
            c = conn.cursor()
            l = [val for val in c.execute("SELECT * FROM leaderboard ORDER BY score DESC")]
            return render_template("leader_board.html", title="Leader Board", leaderboard=l,
                            highlight=request.form["username"])
        else:
            return False

    return render_template("game.html", title="Game", win_point=1, form=form, anon=anon)


@app.route('/leader_board')
def leader_board():
    conn = sqlite3.connect('pong.db')
    c = conn.cursor()
    l = [val for val in c.execute("SELECT * FROM leaderboard ORDER BY score DESC")]
    return render_template("leader_board.html", title="Leader Board", leaderboard=l, highlight="")

if __name__ == "__main__":
    app.run()