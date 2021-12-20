---
title: "Pytest for testing"
author: "Kedar Dabhadkar"
date: 2021-06-09T05:46:18.464519
description: "How you can use Pytest to test your Python code"
type: technical_note
draft: false
---
## Pytest for Unit-Testing Python code

Every line line of code is one more reason why your entire software might crash. We sometimes don't realize the importance of testing our code until our code becomes a part of a production codebase. Pytest is the most widely used framework for unit testing in Python. Here's how you can easily unit test your code with pytest.


```python
# !pip install pytest
```

### Write the code and corresponding tests

As an example, let's write a simple function to check if a number is even. This function returns Boolean - True or False. Let's pass a test case and see if it returns the results that we expect.


```python
%%writefile check_if_even.py

def check_if_even(a):
    """
    Returns True if a is an even number
    """
    return a % 2 == 0

def test_check_if_even():
    """
    Define test cases
    """
    # a = 2. Expected value is True
    a = 2
    is_even = check_if_even(a)
    assert is_even == True
```

    Overwriting check_if_even.py
    

### Run the test

Pytest reads the Python scripts and understands that any function that starts with 'test_' is the test function.


```python
!pytest check_if_even.py
```

    [1m============================= test session starts ==============================[0m
    platform linux -- Python 3.7.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/kedardabhadkar/Notes/data_wrangling/data_manipulation
    plugins: anyio-2.0.2, Faker-8.5.1, dash-1.20.0
    collected 1 item                                                               [0m
    
    check_if_even.py [32m.[0m[32m                                                       [100%][0m
    
    [32m============================== [32m[1m1 passed[0m[32m in 0.04s[0m[32m ===============================[0m
    

### Run multiple tests cases at once


```python
%%writefile check_if_even.py

import pytest

testdata = [
    (2, True),
    (3, False),
    (4, True),
    (5, True) # We expect this test to fail
    ]

def check_if_even(a):
    """
    Returns True if 'a' is an even number
    """
    return a % 2 == 0

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_check_if_even(sample, expected_output):
    """
    Define test cases
    """

    assert check_if_even(sample) == expected_output
```

    Overwriting check_if_even.py
    


```python
!pytest check_if_even.py
```

    [1m============================= test session starts ==============================[0m
    platform linux -- Python 3.7.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/kedardabhadkar/Notes/data_wrangling/data_manipulation
    plugins: anyio-2.0.2, Faker-8.5.1, dash-1.20.0
    collected 4 items                                                              [0m
    
    check_if_even.py [32m.[0m[32m.[0m[32m.[0m[31mF[0m[31m                                                    [100%][0m
    
    =================================== FAILURES ===================================
    [31m[1m__________________________ test_check_if_even[5-True] __________________________[0m
    
    sample = 5, expected_output = True
    
        [37m@pytest[39;49;00m.mark.parametrize([33m'[39;49;00m[33msample, expected_output[39;49;00m[33m'[39;49;00m, testdata)
        [94mdef[39;49;00m [92mtest_check_if_even[39;49;00m(sample, expected_output):
            [33m"""[39;49;00m
        [33m    Define test cases[39;49;00m
        [33m    """[39;49;00m
        
    >       [94massert[39;49;00m check_if_even(sample) == expected_output
    [1m[31mE       assert False == True[0m
    [1m[31mE        +  where False = check_if_even(5)[0m
    
    [1m[31mcheck_if_even.py[0m:23: AssertionError
    =========================== short test summary info ============================
    FAILED check_if_even.py::test_check_if_even[5-True] - assert False == True
    [31m========================= [31m[1m1 failed[0m, [32m3 passed[0m[31m in 0.14s[0m[31m ==========================[0m
    

And as expected, the first 3 test cases passed and the last one failed!

### How do we structure our code after integrating with pytest?

Although there are multiple ways in which you can structure your code, this is the way that I personally prefer it. This structure logically separates your tests from the rest of the source code.


```python
project/
├── src
│   └── check_if_even.py
└── tests
    └── test_code.py
```

When applied to our toy example, this is what each of these two scripts would look like 


```python
%%writefile project/src/check_if_even.py

def check_if_even(a):
    """
    Returns True if 'a' is an even number
    """
    return a % 2 == 0
```

    Overwriting project/src/check_if_even.py
    


```python
%%writefile project/tests/test_code.py

import pytest

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from src.check_if_even import check_if_even

testdata = [
    (2, True),
    (3, False),
    (4, True),
    (5, True) # We expect this test to fail
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_check_if_even(sample, expected_output):
    """
    Define test cases
    """

    assert check_if_even(sample) == expected_output
```

    Overwriting project/tests/test_code.py
    


```python
!pytest project/tests/test_code.py
```

    [1m============================= test session starts ==============================[0m
    platform linux -- Python 3.7.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/kedardabhadkar/Notes/data_wrangling/data_manipulation
    plugins: anyio-2.0.2, Faker-8.5.1, dash-1.20.0
    collected 4 items                                                              [0m
    
    project/tests/test_code.py [32m.[0m[32m.[0m[32m.[0m[31mF[0m[31m                                          [100%][0m
    
    =================================== FAILURES ===================================
    [31m[1m__________________________ test_check_if_even[5-True] __________________________[0m
    
    sample = 5, expected_output = True
    
        [37m@pytest[39;49;00m.mark.parametrize([33m'[39;49;00m[33msample, expected_output[39;49;00m[33m'[39;49;00m, testdata)
        [94mdef[39;49;00m [92mtest_check_if_even[39;49;00m(sample, expected_output):
            [33m"""[39;49;00m
        [33m    Define test cases[39;49;00m
        [33m    """[39;49;00m
        
    >       [94massert[39;49;00m check_if_even(sample) == expected_output
    [1m[31mE       assert False == True[0m
    [1m[31mE        +  where False = check_if_even(5)[0m
    
    [1m[31mproject/tests/test_code.py[0m:25: AssertionError
    =========================== short test summary info ============================
    FAILED project/tests/test_code.py::test_check_if_even[5-True] - assert False ...
    [31m========================= [31m[1m1 failed[0m, [32m3 passed[0m[31m in 0.14s[0m[31m ==========================[0m
    

### Read more

[1] https://towardsdatascience.com/pytest-for-data-scientists-2990319e55e6 <br>
[2] https://docs.pytest.org/en/6.2.x/
