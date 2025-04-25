from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route()

#add_url_rule(<url rule>, <endpoint>, <view function>)