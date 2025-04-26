from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class MyForm(FlaskForm):
    name = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class SignupForm(FlaskForm):
    name = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

@app.route('/')
def index():
    form = MyForm()
    signup = SignupForm()
    if form.validate_on_submit():
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

#add_url_rule(<url rule>, <endpoint>, <view function>)