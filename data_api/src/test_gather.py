from gather import *

def test_stats_add():
    # Normal case
    a = {"additions": 1,"changes": 2,"deletions": 1,}
    b = {"additions": 2,"changes": 3,"deletions": 1,}

    stats_add(a,b)
    assert a["additions"] == 3
    assert a["changes"] == 5
    assert a["deletions"] == 2

    # Case with 0
    a = {"additions": 0,"changes": 1,"deletions": 1,}
    b = {"additions": 2,"changes": 3,"deletions": 1,}

    stats_add(a,b)

    assert a["additions"] == 2
    assert a["changes"] == 4
    assert a["deletions"] == 2

def test_normalize_commit_stat():
    # Normal case
    c = {
        "_id": "testid",
        "repo_name": "test_repo_name",
        "date": "2021/11/26",
        "granularity": "by_day",
        "contributor": "SamuelAl",
        "stats": {"additions": 1,"changes": 2,"deletions": 1,}
    }
    normalize_commit_stat(c)
    norm_stat = c["stats"]
    assert norm_stat["additions"] == 0.5
    assert norm_stat["changes"] == 2
    assert norm_stat["deletions"] == 0.5

    # Case with division by 0
    c["stats"] = {"additions": 0,"changes": 0,"deletions": 0,}
    normalize_commit_stat(c)
    norm_stat = c["stats"]
    assert norm_stat["additions"] == 0
    assert norm_stat["changes"] == 0
    assert norm_stat["deletions"] == 0

def test_get_repo_contributors():
    # Get a personal repo with a single contributor
    arr = get_repo_contributors("SamuelAl/test_repo")
    assert len(arr) == 1
    assert arr[0]["name"] == "SamuelAl"
    assert arr[0]["avatar_url"] == "https://avatars.githubusercontent.com/u/33717014?v=4"

    # Get repo with multiple contributors
    arr = get_repo_contributors("SamuelAl/Clothes-Annotation-Web-App")
    assert len(arr) == 7



