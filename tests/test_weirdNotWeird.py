from scripts.weirdNotWeird import weirdNotWeird


def test_odd_no_prints_Weid():
    n = 3
    assert weirdNotWeird(n) == 'Weird'
    n = 9
    assert weirdNotWeird(n) == 'Weird'
    n = 21
    assert weirdNotWeird(n) == 'Weird'


def test_even_no_and_in_range_2_to_5_print_Not_weird():
    n = 2
    assert weirdNotWeird(n) == 'Not weird'


def test_even_no_and_in_range_6_to_20_print_Weird():
    n = 6
    assert weirdNotWeird(n) == 'Weird'
    n = 20
    assert weirdNotWeird(n) == 'Weird'
