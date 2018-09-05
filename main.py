from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(app.config)
db = SQLAlchemy(app)

from models import Comment

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        client_ip = request.remote_addr
        db.session.add(
            Comment(text=comment, client_ip=client_ip)
        )
        db.session.commit()
    comments = db.session.query(Comment).all()
    return render_template('comments/index.html', comments=comments)

if __name__ == '__main__':
    app.run()