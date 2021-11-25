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

@app.route('/api/repo/', methods=['GET','POST'])
def get_stats_from_params():
    repo = request.args.get('repo')
    user = request.args.get('user')
    normalize = request.args.get('normalize') == "true"
    print(f'Getting info for Repo: {repo}; User: {user}; Normalize: {normalize}')
    if user is None:
        user = ALL_AUTHORS

    return jsonpickle.encode(get_commit_stats(repo, user, normalize))


@app.route('/api/repo/contributors', methods=['GET','POST'])
def get_contributors():
    repo = request.args.get('repo')
    print(f'Getting info for Repo: {repo}')
    return jsonpickle.encode(get_repo_contributors(repo))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)


