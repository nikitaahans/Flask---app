import flask
print(flask.__version__)

from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

# Adding HTML to the page
from flask import render_template

app = Flask(__name__)
#
@app.route('/')
def about():
    return 'Hello World'

@app.route('/home/')
def home():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()