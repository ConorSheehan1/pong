from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("game.html", title="game", win_point=2)
    # return render_template("template.html", score1=0)


@app.route('/leader_board')
def leader_board():
    return render_template("leader_board.html", title="leader board", win_point=2)

if __name__ == "__main__":
    app.debug = True
    app.run()