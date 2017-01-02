from flask import Flask, render_template, request, flash
from flask_login import login_user, login_required, logout_user
from flask_heroku import Heroku
app = Flask(__name__)
heroku = Heroku(app)


@app.route('/')
def home_page():
    return render_template("index.html", title="home")


@app.route("/log_in", methods=["GET", "POST"]) # route for handling the login page logic. view function accepts both GET and POST requests
def log_in():
    pg_name = "Login"
    error = None
    form = request.form # create instance of LoginForm request.form
    if request.method == "POST" and form.validate_on_submit():
        # user = Users.query.filter_by(username=request.form["username"]).first()
        # if user is not None and user.check_password(form.password.data):
        #     login_user(user)
        #     flash("User %s logged in successfully" % (form.username.data)) # returns a message on next page to user
        #     return game_page() # redirect tells the client web browser to navigate to a different page
        if False:
            print("do nothing")
        else:
            error = "Invalid user credentials. Please try again."
    return render_template("log_in.html", pg_name=pg_name, title="Sign In", form=form, error=error) # pass LoginForm object to template


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