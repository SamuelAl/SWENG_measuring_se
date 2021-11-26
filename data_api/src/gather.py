from datetime import datetime
from github import Github
import json
import jsonpickle
import pprint
import pymongo

ALL_AUTHORS = "all"

g = Github("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")

# Establish connection to database

client = pymongo.MongoClient('localhost', 27017)

db = client.github_database
repos_collection = db.repos
repos_collection.create_index([("repo_name", pymongo.ASCENDING)], unique=True)
commit_stats_collection = db.commit_stats

def stats_add(a, b):
    a["additions"] += b["additions"]
    a["changes"] += b["changes"]
    a["deletions"] += b["deletions"]

def normalize_commit_stat(commit_stat):
    stat = commit_stat["stats"]
    if stat["changes"] == 0:
        return commit_stat
    
    stat["additions"] /= stat["changes"]
    stat["deletions"] /= stat["changes"]
    commit_stat["stats"] = stat
    return commit_stat

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


def get_commit_stats_from_api(repo_name):
    commits_dct = {}
    commits = get_repo_commits(repo_name)
    # Get commit stats
    for commit in commits:
        author = commit.author.login
        files = commit.files
        stats = calculate_commit_stats(files)
        date = commit.commit.author.date
        date_str = date.strftime("%Y/%m/%d")
        if date_str in commits_dct:
            date_dct = commits_dct[date_str]
        else:
            date_dct = {}
            date_dct[ALL_AUTHORS] = {
                "additions": 0, "changes": 0, "deletions": 0}

        if author in date_dct:
            author_stats = date_dct[author]
        else:
            author_stats = {"additions": 0, "changes": 0, "deletions": 0}

        general_stats = date_dct[ALL_AUTHORS]

        stats_add(general_stats, stats)
        stats_add(author_stats, stats)

        date_dct[ALL_AUTHORS] = general_stats
        date_dct[author] = author_stats
        commits_dct[date_str] = date_dct

    commit_stats_arr = []
    for date, stats in commits_dct.items():
        for user, stat in stats.items():
            commit_stat_doc = {
                "_id": repo_name + user + date,
                "repo_name": repo_name,
                "date": date,
                "granularity": "by_day",
                "contributor": user,
                "stats": stat
            }
            commit_stats_arr.append(commit_stat_doc)

    return commit_stats_arr


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

# get_commit_stats("SamuelAl/hexbin", "SamuelAl")
