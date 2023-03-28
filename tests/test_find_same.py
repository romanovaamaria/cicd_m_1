from main import find_same
import pytest

def test_check_if_same_while_same():
    file_list1 = ["1\n", "2\n"]
    file_list2 = ["2\n", "1\n",]
    expected_output = ["1\n", "2\n"]
    find_same(file_list1, file_list2)
    with open('same.txt') as f:
        assert f.readlines() == expected_output

def test_check_if_same_while_diff():
    file_list1 = ["1\n", "2\n"]
    file_list2 = ["3\n", "4\n",]
    expected_output = []
    find_same(file_list1, file_list2)
    with open('same.txt') as f:
        assert f.readlines() == expected_output