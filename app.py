from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from time import gmtime, strftime
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Comment

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        client_ip = request.remote_addr
        time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        print(comment, client_ip, time)
    return render_template('comments/index.html')

if __name__ == '__main__':
    app.run()