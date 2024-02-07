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


