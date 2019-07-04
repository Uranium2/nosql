from flask import Flask, request, render_template, send_from_directory, url_for
import os
import sys
from flask_material import Material  

app = Flask(__name__)
Material(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    print("test")
    return render_template('index.html')

@app.route('/handle_movie/', methods=['POST'])
def handle_movie():
    movie_name = request.form['movie']
    print(movie_name)
    return render_template("result.html")

@app.route('/handle_actor/', methods=['POST'])
def handle_actor():
    actor_name = request.form['actor']
    print(actor_name)
    return render_template("result.html")
    

if __name__ == "__main__":
    app.run(debug=False, host= '0.0.0.0')