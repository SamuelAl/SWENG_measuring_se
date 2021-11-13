from github import Github
import json
import pprint
# import pymongo

g = Github("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")

# Get all repos from my account
repos = g.get_user("SamuelAl").get_repo()
for repo in repos:
    pprint.pprint(repo)



