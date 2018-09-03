from flask import Flask, request, render_template
from time import gmtime, strftime
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        client_ip = request.remote_addr
        time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        print(comment, client_ip, time)
    return render_template('comments/index.html')
