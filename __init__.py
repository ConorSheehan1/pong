from flask import Flask, render_template, request, flash
from flask_heroku import Heroku
from forms import SubmitForm
import sqlite3
app = Flask(__name__)
app.config.from_object("config.TestingConfig")
heroku = Heroku(app)


@app.route('/')
def home_page():
    return render_template("./index.html", title="home")


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
        print("here")
        submit_score(request.form["username"], request.form["score"])
        # conn = sqlite3.connect('pong.db')
        # c = conn.cursor()
        # c.execute("INSERT INTO leaderboard "
        #       "values (?, ?)", (request.form["username"], request.form["score"]))
        #
        # conn.commit()
        # conn.close()
        # print("commited", form.username.data, form.score.data, "to db")

    return render_template("game.html", title="game", win_point=1, form=form)
    # return render_template("template.html", score1=0)


@app.route('/leader_board')
def leader_board():
    return render_template("leader_board.html", title="leader board")

if __name__ == "__main__":
    app.debug = True
    app.run()