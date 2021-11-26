from datetime import datetime
from gather_helpers import *
import pymongo

# Establish connection to database

client = pymongo.MongoClient('localhost', 27017)

db = client.github_database
repos_collection = db.repos
repos_collection.create_index([("repo_name", pymongo.ASCENDING)], unique=True)
commit_stats_collection = db.commit_stats

def get_commit_stats(repo_name, user, normalize):
    is_in_db = repos_collection.count_documents({"repo_name": repo_name}) >= 1
    stats = []
    if is_in_db:
        stats_raw = commit_stats_collection.find(
            {"repo_name": repo_name, "contributor": user})
        for stat in stats_raw:
            if normalize:
                stat = normalize_commit_stat(stat)
            stats.append(stat)
    else:
        repo_doc = {
            "repo_name": repo_name,
            "contributors": get_repo_contributors(repo_name),
        }
        repos_collection.insert_one(repo_doc)
        unfltr_stats = get_commit_stats_from_api(repo_name)
        commit_stats_collection.insert_many(unfltr_stats)
        if normalize:
            stats = [normalize_commit_stat(a) for a in unfltr_stats if a["contributor"] == user]
        else:
            stats = [a for a in unfltr_stats if a["contributor"] == user]

    return stats

def get_repo_contributors_data(repo_name):
    is_in_db = repos_collection.count_documents({"repo_name": repo_name}) >= 1
    if is_in_db:
        repo_data = repos_collection.find_one({"repo_name": repo_name})
        contributors = repo_data["contributors"]
        return contributors
    else:
        repo_doc = {
            "repo_name": repo_name,
            "contributors": get_repo_contributors(repo_name),
        }
        repos_collection.insert_one(repo_doc)
        unfltr_stats = get_commit_stats_from_api(repo_name)
        commit_stats_collection.insert_many(unfltr_stats)
        return repo_doc["contributors"]

