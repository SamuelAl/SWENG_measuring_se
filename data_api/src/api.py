import os
from flask import Flask, request
from flask_cors import CORS
import jsonpickle
from gather import *
from gather_helpers import *

app = Flask(__name__)
cors = CORS(app)

print(os.environ["TOKEN"])

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
    app.run(host='0.0.0.0', port=5000)


