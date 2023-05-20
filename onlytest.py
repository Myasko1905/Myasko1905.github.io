def multiply(x, y):
    return x * y
    
    
def sum_vals(x, y):
    return x + y
    
    
def add_hello(string):
    return string + 'hello'

def square(x):
    return x*x
    
    
cache = {0: 0, 1: 1}
def fibonacci_of(n):
    if n in cache:  
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]

def test_square():
    assert square(4) == 16

# TESTS ==========================================================================
def test_fibonacci_of():
    #0 1 1 2 3 5 8 13 21 34 55 89 144 - Первые несколько чисел Фибоначчи
    assert fibonacci_of(0) == 0
    assert fibonacci_of(1) == 1
    assert fibonacci_of(2) == 1
    assert fibonacci_of(3) == 2
    assert fibonacci_of(4) == 3
    assert fibonacci_of(5) == 5
    assert fibonacci_of(6) == 8
    
def test_multiply():
    assert multiply(5, 5) == 25
    assert multiply(0, 5) == 0
    assert multiply(-5, 5) == -25
    
def test_vals():
    assert sum_vals(5, 5) == 10
    assert sum_vals(0, 5) == 5
    assert sum_vals(-5, 5) == 0
    
def test_add_hello():
    assert add_hello("привет") == "приветhello"
    assert add_hello('hello') == 'hellohello'
    #Wassert add_hello(-5) == '-5hello'

