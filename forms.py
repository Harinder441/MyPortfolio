from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators,SubmitField,PasswordField


class UserForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    massage = TextAreaField('Message', [validators.DataRequired()],render_kw={'rows':5})
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
