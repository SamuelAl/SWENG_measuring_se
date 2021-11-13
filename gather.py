from github import Github
import json
import pprint
# import pymongo

g = Github("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")

def get_user_repos(usr_name):
    return g.get_user("usr_name")

# Get info for a specific repo (SamuelAl/GraphApp-Stocks-Visualizer)
repo_name = "SamuelAl/libfive"
libfive = g.get_repo(repo_name)
for commit in libfive.get_commits():
    pprint.pprint(commit)



