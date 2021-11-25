from datetime import datetime
from github import Github
import json
import jsonpickle
import pprint
import pymongo

ALL_AUTHORS = "all"

g = Github("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") #you know what to do

client = pymongo.MongoClient('localhost', 27017)
db = client.github_data
repos = db.repo_collection


def calculate_commit_stats(files):
    stats = {
        "additions": 0,
        "deletions": 0, 
        "changes": 0,
    }
    for file in files:
        stats["additions"] += file.additions
        stats["changes"] += file.changes
        stats["deletions"] += file.deletions
    return stats

def get_user_repos(usr_name):
    return g.get_user("usr_name")

def get_repo_commits(repo_name):
    return g.get_repo(repo_name).get_commits()

def get_repo_contributors(repo_name):
    contributors_arr = [] 
    contributors = g.get_repo(repo_name).get_contributors()
    for contributor in contributors:
        c_dct = {
            "name": contributor.login,
            "avatar_url": contributor.avatar_url
        }
        contributors_arr.append(c_dct)
    return contributors_arr

def get_commit_stats_mongo(repo_name, user, normalized):
    repo_dct = {
        "name": repo_name,
        "commits": {}
    } 
    # Get contributors
    repo_dct["contributors"] = get_repo_contributors(repo_name)
    commits = get_repo_commits(repo_name)

    # Get commit stats
    for commit in commits:
        author = commit.author.login
        files = commit.files
        stats = calculate_commit_stats(files)
        date = commit.commit.author.date
        # date_str = date.strftime("%Y/%m/%d")
        if date in repo_dct["commits"]:
            date_dct = repo_dct["commits"][date]
        else:
             date_dct = {}
             date_dct[ALL_AUTHORS] = {"additions": 0, "changes": 0, "deletions": 0}
        
        if author in date_dct:
            author_stats = date_dct[author]
        else:
            author_stats = {"additions": 0, "changes": 0, "deletions": 0}

        general_stats = date_dct[ALL_AUTHORS]

        stats_add(general_stats,stats)
        stats_add(author_stats,stats)

        date_dct[ALL_AUTHORS] = general_stats
        date_dct[author] = author_stats
        repo_dct["commits"][date] = date_dct 
    
    pprint.pprint(jsonpickle.encode(repo_dct))
    
    # Prepare for mongo storage
    
    
    
    return date_dct

def stats_add(a, b):
    a["additions"] += b["additions"]
    a["changes"] += b["changes"]
    a["deletions"] += b["deletions"]

get_commit_stats_mongo("SamuelAl/hexbin", "", True)




