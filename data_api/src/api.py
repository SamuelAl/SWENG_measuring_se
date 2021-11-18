from flask import Flask
import jsonpickle
from gather import *

app = Flask(__name__)

@app.route('/hello/', methods=['GET','POST'])
def welcome():
    return "Hello!"

@app.route('/data/user/<string:username>/repo/<string:repo_name>/', methods=['GET','POST'])
def get_stats(username,repo_name):
    full_repo_name = username + "/" + repo_name
    return jsonpickle.encode(get_commit_stats_by_date(full_repo_name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)


