from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", title="Pong", win_point=2)
    # return render_template("template.html", score1=0)

if __name__ == "__main__":
    app.debug = True
    app.run()