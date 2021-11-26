from gather import *

def test_stats_add():
    a = {"additions": 1,"changes": 2,"deletions": 1,}
    b = {"additions": 2,"changes": 3,"deletions": 1,}

    stats_add(a,b)
    assert a["additions"] == 3
    assert a["changes"] == 5
    assert a["deletions"] == 2

    a = {"additions": 0,"changes": 1,"deletions": 1,}
    b = {"additions": 2,"changes": 3,"deletions": 1,}

    stats_add(a,b)

    assert a["additions"] == 2
    assert a["changes"] == 4
    assert a["deletions"] == 2


