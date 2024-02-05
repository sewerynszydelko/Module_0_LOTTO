from lotto import get_random_6_nums


def test_get_random_6_nums_list():
    random_6_list = get_random_6_nums()

    assert random_6_list is list
