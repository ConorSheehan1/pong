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


@app.route('/submit_score', methods=['GET', 'POST'])
def submit_score():
    error = None
    form = SubmitForm()
    # if username isn't already on leaderboard, add score to db
    if request.method == "POST" and form.validate_on_submit():
        conn = sqlite3.connect('pong.db')
        c = conn.cursor()
        c.execute("INSERT INTO leaderboard "
          "values (?, ?)", ("me", 0))

        conn.commit()
        conn.close()
    return render_template("submit_form.html", title="submit", form=form, error=error)


@app.route('/game', methods=['GET', 'POST'])
def game_page():

    error = None
    form = SubmitForm()
    user = request.args.get('user', 0, type=int)
    computer = request.args.get('computer', 0, type=int)
    if request.method == "POST" and form.validate_on_submit():
        if user is None:
            # flash("Score %s for user %s was logged successfully" % (form.score.data, form.username.data))
            return game_page()
        else:
            error = "Error" + form.username.data + "already exists, please choose a different name."
            print(error)

    return render_template("game.html", title="game", win_point=2, form=form, error=error)
    # return render_template("template.html", score1=0)


@app.route('/leader_board')
def leader_board():
    return render_template("leader_board.html", title="leader board")

if __name__ == "__main__":
    app.debug = True
    app.run()