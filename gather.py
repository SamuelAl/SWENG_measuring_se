from github import Github
import json
import pprint
# import pymongo

g = Github("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")

def get_user_repos(usr_name):
    return g.get_user("usr_name")

def get_repo_commits(repo_name):
    return g.get_repo(repo_name).get_commits()





