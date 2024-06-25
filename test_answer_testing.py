
from answer_testing_ferst_kt import concat_total
from answer_testing_for_json import *
import pytest
import filecmp

@pytest.mark.parametrize('avg, avg_in_grades',concat_total())
def test_avg(avg, avg_in_grades):
    assert avg == avg_in_grades


@pytest.mark.smoke
def test_comprasion_file_json_and_new_file():
    result = filecmp.cmp(INPUT_FILE,OUTPUT_FILE,shallow=False)
    assert result == True

@pytest.mark.smoke
def test_comprasion_new_file_and_sort_file():
    result = filecmp.cmp(SORT_FILE,OUTPUT_FILE,shallow=False)
    assert result == True
