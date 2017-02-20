from flask import Flask, render_template, request, flash, redirect
from flask_heroku import Heroku
from forms import SubmitForm
import sqlite3
app = Flask(__name__)
app.config.from_object("config.Test")
# app.config.from_object("config.Production")
heroku = Heroku(app)


def helper_submit_score(username, score):
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


def helper_get_leaderboard():
    conn = sqlite3.connect('pong.db')
    c = conn.cursor()
    # use enumerate to generate rank for users.
    # Ties will be broken by time i.e. the first user to get a given score will appear highest
    return [val for val in enumerate(c.execute("SELECT * FROM leaderboard ORDER BY score DESC"))]


@app.route('/')
def home_page():
    return render_template("./index.html", title="Home")


@app.route('/game', methods=['GET', 'POST'])
def game_page():

    # count number of players in database and assign that number +1 to default anon name
    conn = sqlite3.connect('pong.db')
    c = conn.cursor()
    names = [tup[0] for tup in c.execute("SELECT user_name FROM leaderboard")]
    conn.close()

    form = SubmitForm()
    if form.validate_on_submit():
        submitted = helper_submit_score(request.form["username"], request.form["score"])

        # if value submits successfully to database, redirect to leaderboard and highlight row added
        if submitted:
            return render_template("leader_board.html", title="Leader Board", leaderboard=helper_get_leaderboard(),
                                   highlight=request.form["username"], play_again=True)
        else:
            flash("an error occurred submitting to the database")

    return render_template("game.html", title="Game", win_point=1, ai_speed=5, form=form, names=names)


@app.route('/leader_board')
def leader_board():
    return render_template("leader_board.html", title="Leader Board", leaderboard=helper_get_leaderboard())

if __name__ == "__main__":
    app.run()