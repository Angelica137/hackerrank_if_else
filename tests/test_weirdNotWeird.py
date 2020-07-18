from scripts.weirdNotWeird import weirdNotWeird


def test_odd_no_prints_Weid():
    n = 3
    assert weirdNotWeird(n) == 'Weird'
