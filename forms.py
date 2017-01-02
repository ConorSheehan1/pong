from flask_wtf import Form, RecaptchaField
from wtforms import StringField, validators
import sqlite3


def unique_user(form, field):
    '''
    when a user tries to submit a score to the leaderboard, they must use a unique name
    '''

    conn = sqlite3.connect('pong.db')
    c = conn.cursor()
    user = [val for val in c.execute("SELECT * FROM leaderboard WHERE user_name = (?)", (form.username.data,))]

    # if the name is in the database already throw an error
    if user != []:
        print("user", user, user != [])
        raise validators.ValidationError('This name is taken, please choose a different one.')


class SubmitForm(Form):
    username = StringField('name', [validators.DataRequired(), unique_user])
    recaptcha = RecaptchaField()


