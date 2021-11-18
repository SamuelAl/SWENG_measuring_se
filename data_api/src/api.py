from flask import Flask
import jsonpickle
from gather import *

app = Flask(__name__)

@app.route('/hello/', methods=['GET','POST'])
def welcome():
    return "Hello!"

@app.route('/data/', methods=['GET','POST'])
def get_stats():
    return jsonpickle.encode(get_commit_stats_by_date("SamuelAl/hexbin"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

#for k,v in get_commit_stats_by_date("SamuelAl/hexbin").items():
#    print(k)
#    print(v)

