import sys
import os
sys.path.append(os.path.abspath(
    "C:\\Users\\5792\\Desktop\\Module_0_Lotto\\scripts"))
from lotto import get_random_6_nums, get_user_num, cost_and_years_to_win


def test_get_random_6_nums_list():
    random_6_list = get_random_6_nums()

    assert type(random_6_list) is set

def test_get_user_num_is_list():    
    assert type(get_user_num()) is set

def test_cost_and_years_to_win():
    count_trys_temporaly = 100
    info = cost_and_years_to_win(count_trys=count_trys_temporaly)

    assert type(info) is str
