import math_functions

def test_fib():
    assert math_functions.fib(0) == 0
    assert math_functions.fib(1) == 1
    assert math_functions.fib(2) == 1
    assert math_functions.fib(10) == 55


def test_prime():
    assert math_functions.is_prime(2) == True
    assert math_functions.is_prime(5) == True
    assert math_functions.is_prime(7) == True
    assert math_functions.is_prime(9) == False
    assert math_functions.is_prime(11) == True
    assert math_functions.is_prime(13) == True
    assert math_functions.is_prime(100000007) == True


def test_hex():
    assert math_functions.hex_to_dec('A') == 10
    assert math_functions.hex_to_dec('F') == 15
    assert math_functions.hex_to_dec('10') == 16
    assert math_functions.hex_to_dec('2B') == 43
    assert math_functions.hex_to_dec('B2') == 178



def test_hex():
    assert math_functions.hex_to_decimal('A') == 10
    assert math_functions.hex_to_decimal('F') == 15
    assert math_functions.hex_to_decimal('10') == 16
    assert math_functions.hex_to_decimal('2B') == 43
    assert math_functions.hex_to_decimal('B2') == 178
    assert math_functions.hex_to_decimal('3A2') == 930