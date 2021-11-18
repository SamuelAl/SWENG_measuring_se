from datetime import datetime
from github import Github
import json
import pprint
# import pymongo

g = Github("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") #you know what to do

class CommitStats:
    def __init__(self, additions, changes, deletions):
        self.additions = additions
        self.changes = changes
        self.deletions = deletions

    def __str__(self):
        return f'Additions: {self.additions}; Changes: {self.changes}; Deletions: {self.deletions}'

def calculate_commit_stats(files):
    stats = CommitStats(0,0,0)
    for file in files:
        stats.additions += file.additions
        stats.changes += file.changes
        stats.deletions += file.deletions
    return stats

def get_user_repos(usr_name):
    return g.get_user("usr_name")

def get_repo_commits(repo_name):
    return g.get_repo(repo_name).get_commits()

def get_commit_stats_by_date(repo_name):
    date_dct = {} 
    commits = get_repo_commits(repo_name)
    print(commits.totalCount)
    for commit in commits:
        files = commit.files
        stats = calculate_commit_stats(files)
        date = commit.commit.author.date
        date_str = date.strftime("%Y/%m/%d")
        if date_str in date_dct:
            date_stats = date_dct[date_str]
            date_stats.additions += stats.additions
            date_stats.changes += stats.changes
            date_stats.deletions += stats.deletions
            date_dct[date_str] = date_stats
        else:
            date_dct[date_str] = CommitStats(stats.additions,stats.changes,stats.deletions)
    return date_dct







