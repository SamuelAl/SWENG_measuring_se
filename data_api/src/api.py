from flask import Flask, request
from flask_cors import CORS
import jsonpickle
from gather import *

app = Flask(__name__)
cors = CORS(app)

dummy_data = {
    "2021/01/01": {
        "additions": 0.5,
        "changes":56,
        "deletions":0.5,
    },
     "2021/02/01": {
        "additions": 0.2,
        "changes":56,
        "deletions":0.8,
    },
     "2021/03/01": {
        "additions": 0.6,
        "changes":56,
        "deletions":0.4,
    },
     "2021/04/01": {
        "additions": 0.5,
        "changes":56,
        "deletions":0.5,
    },
     "2021/05/01": {
        "additions": 0.7,
        "changes":56,
        "deletions":0.3,
    },
     "2021/06/01": {
        "additions": 0.4,
        "changes":56,
        "deletions":0.6,
    }

}

@app.route('/hello/', methods=['GET','POST'])
def welcome():
    return "Hello!"

@app.route('/data/user/<string:username>/repo/<string:repo_name>/', methods=['GET','POST'])
def get_stats(username,repo_name):
    #full_repo_name = username + "/" + repo_name
    #return jsonpickle.encode(get_commit_stats_by_date(full_repo_name))
    return jsonpickle.encode(dummy_data)


@app.route('/api/repo/', methods=['GET','POST'])
def get_stats_from_params():
    repo = request.args.get('repo')
    user = request.args.get('user')
    print(f'Repo: {repo}; User: {user}')
    return jsonpickle.encode(dummy_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)


