import sys
import os
sys.path.append(os.path.abspath(
    "C:\\Users\\5792\\Desktop\\Module_0_Lotto\\scripts"))
from lotto import get_random_6_nums


def test_get_random_6_nums_list():
    random_6_list = get_random_6_nums()

    assert type(random_6_list) is list
