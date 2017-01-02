from flask import Flask, render_template, request, flash
from flask_heroku import Heroku
from forms import SubmitForm
import sqlite3
app = Flask(__name__)
app.config.from_object("config.TestingConfig")
heroku = Heroku(app)


@app.route('/')
def home_page():
    return render_template("index.html", title="home")


@app.route("/submit_form", methods=["GET", "POST"]) # route for handling the login page logic. view function accepts both GET and POST requests
def submit_score():
    print("go")
    error = None # start with no error
    form = SubmitForm() # create instance form
    conn = sqlite3.connect('pong.db') # connect to db
    if request.method == "POST" and form.validate_on_submit():
        user = conn.cursor().execute("SELECT user_name FROM users where user_name = (?)", form.username.data)
        print("user", user)
        if user is None:
            flash("Score %s for user %s logged successfully" % (form.score.data, form.username.data)) # returns a message on next page to user
            return game_page() # redirect tells the client web browser to navigate to a different page
        else:
            error = "Error" + form.username.data + "already exists, please choose a different name."
            print(error)
    return render_template("submit_form.html", title="submit", form=form, error=error)


@app.route('/game')
def game_page():
    return render_template("game.html", title="game", win_point=2)
    # return render_template("template.html", score1=0)


@app.route('/leader_board')
def leader_board():
    return render_template("leader_board.html", title="leader board")

if __name__ == "__main__":
    app.debug = True
    app.run()