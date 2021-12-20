---
title: "Build a local Python package"
author: "Kedar Dabhadkar"
date: 2021-05-23T05:46:18.464519
description: "Build a local Python package"
type: technical_note
draft: false
---
### Build a Local Python Package

How do you ensure that you reduce redundancy when writing Python code? Think about that Matplotlib code that you once wrote to add a cool new element to your charts, or the number of times you had to copy-paste the server name of your database. Did you know that you can avoid that repetition by installing a locally built Python package across your environment?

Let me demonstrate how you can do that using just the most basic code required.

Let's build a Python package named 'toolbox' and include a function to find the roots of a quadratic equation.

#### Step 1. Build this directory structure
- toolbox/
    - setup.py
    - toolbox/
        - \__init__.py
        - roots.py
#### Step 2. Write your Python function

Populate roots.py with your repetitive code. In my case, the function to find out roots of a quadratic


```python
def get_roots_quadratic(a, b, c):
    """
    Returns the roots of a quadratic equation using the coefficients.
    """
    root1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
    root2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
    
    return root1, root2
```

#### Step 4. Populate setup.py

From the root directory, edit setup.py


```python
import setuptools

setuptools.setup(name='toolbox',
                version='0.0.1',
                descrption='Save frequently used scripts',
                packages=setuptools.find_packages(),
                zip_safe=False)
```

#### Step 5. Install your new package

Go to the root directory and install your package


```python
pip install .
```

#### Use your package


```python
from toolbox import roots

get_roots_quadratic(1, -2, 1)
```




    (1.0, 1.0)



#### Read more

Learn about adding additional features and publishing your package to PyPI: https://www.freecodecamp.org/news/build-your-first-python-package/
