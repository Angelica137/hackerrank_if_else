from scripts.weirdNotWeird import weirdNotWeird


def test_odd_no_prints_Weid():
    n = 3
    assert weirdNotWeird(n) == 'Weird'


def test_even_no_and_in_range_2_to_5_print_Not_weird():
    n = 2
    assert weirdNotWeird(n) == 'Not weird'
