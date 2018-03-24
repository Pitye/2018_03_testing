from fb import fizzbuzz
import pytest

def test_fizzbuzz_return_str():
    assert isinstance(fizzbuzz(1),str)

@pytest.mark.parametrize('num', [1,2,4,7,8])
def test_fizzbuzz_regular_return_self(num):
    assert fizzbuzz(num) == str(num)

@pytest.mark.parametrize('num', [3,6,9,12])
def test_fizzbuzz_3div_return_fizz(num):
    assert fizzbuzz(num) == 'fizz'

@pytest.mark.parametrize('num', [5,10])
def test_fizzbuzz_5div_return_buzz(num):
    assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [15])
def test_fizzbuzz_15div_return_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'
