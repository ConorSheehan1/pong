from flask_wtf import Form, RecaptchaField
from wtforms import StringField, validators


class SubmitForm(Form):
    username = StringField('name', [validators.DataRequired()])
    score = StringField('score', [validators.DataRequired()])
    recaptcha = RecaptchaField()