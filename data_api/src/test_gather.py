from gather import *

TEST_REPO_NAME = "SamuelAl/test_repo"

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
    arr = get_repo_contributors(TEST_REPO_NAME)
    assert len(arr) == 1
    assert arr[0]["name"] == "SamuelAl"
    assert arr[0]["avatar_url"] == "https://avatars.githubusercontent.com/u/33717014?v=4"

    # Get repo with multiple contributors
    arr = get_repo_contributors("SamuelAl/Clothes-Annotation-Web-App")
    assert len(arr) == 7

def test_get_commits_from_api():
    # Use test repo 
    arr = get_commit_stats_from_api(TEST_REPO_NAME)

    assert len(arr) == 2

    c_all = c_contributor = []
    if arr[0]["contributor"] == "all":
        c_all = arr[0]
        c_contributor = arr[1]
    else:
        c_all = arr[1]
        c_contributor = arr[0]
    
    # Check contributor field
    assert c_all["contributor"] == "all"
    assert c_contributor["contributor"] == "SamuelAl"

    # Check date field
    assert c_all["date"] == "2021/11/26"
    assert c_contributor["date"] == "2021/11/26"

    # Check granularity
    assert c_all["granularity"] == "by_day"
    assert c_contributor["granularity"] == "by_day"

    # Check stats
    stats_all = c_all["stats"]
    stats_contributor = c_contributor["stats"]

    assert stats_all["additions"] == 1
    assert stats_all["changes"] == 1
    assert stats_all["deletions"] == 0

    assert stats_contributor["additions"] == 1
    assert stats_contributor["changes"] == 1
    assert stats_contributor["deletions"] == 0





