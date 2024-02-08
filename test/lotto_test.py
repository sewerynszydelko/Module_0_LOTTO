from math import radians
import sys
import os
sys.path.append(os.path.abspath(
    "C:\\Users\\5792\\Desktop\\Module_0_Lotto\\scripts"))
from lotto import get_random_6_nums, get_user_num, cost_and_years_to_win


def test_get_random_6_nums_list():
    random_6_list = get_random_6_nums()

    assert type(random_6_list) is set

#def test_get_user_num_is_list():    
#    assert type(get_user_num()) is set

def test_cost_and_years_to_win():
    count_trys_temporaly = 100
    info = cost_and_years_to_win(count_trys=count_trys_temporaly)

    assert type(info) is str

def test_get_random_6_nums():
    get_6_numbers = get_random_6_nums()
    assert len(get_6_numbers) == 6

def test_get_random_6_nums_200_times():

    for _ in range(200):
        get_6_nums = get_random_6_nums()
        result = len(get_6_nums)
        assert result == 6

def test_get_random_6_nums_betwin_1_49():
    random_6 = get_random_6_nums()

    for num in random_6:
        assert num <= 49 and num >= 1