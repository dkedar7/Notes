---
title: "Using FastAPI to Deploy ML Models"
author: "Kedar Dabhadkar"
date: 2021-12-19T05:46:18.464519
description: "Notes on using FastAPI as I go through the online documentation"
type: technical_note
draft: true
---
<h1><center>Using FastAPI to Deploy ML Models</center></h1>
<center><h4>Notes on using FastAPI as I go through the online documentation</h4></center>

<br>
<br>

Kedar Dabhadkar <br>
Data Scientist<br>
linkedin.com/in/dkedar7

## What is FastAPI?

- This is what FastAPI is

## First steps

- This is simply how we define an app and write our first GET request.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

- If this code is saved to main.py, use the follwowing to run it from the command line:
```
uvicorn main:app --reload
```

- FastAPI also automatically generates a Swagger documentation at 'http://127.0.0.1:8000'
 ```


```python

```

## 1. Path parameters

- Path parameters or variables can be defined in the decorator and also as an input to the function.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```
- Value of 'item_id' is passed to the function
- This function is run when a user accesses the endpoint 'http://127.0.0.1:8000/items/3'



- Also, order matters.
- In the following example, although `/users/me` matches with the pattern `/users/{user_id}`, it's executed first because it appears first

```python
@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}
```


```python

```

## 2. Query Parameters

- All the function arguments that are not a part of the path parameters are treated as query parameters.
- Query parameters appear after `?` in a URL and are separated by `&`

```python
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return data[skip : skip + limit]
```

- If a default value is set in the function arguments, these parameters become optional. If not, they are mandatory.

## Multiple path and query parameters

- You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
- They will be detected by name, so the order doesn't matter.
- For example,
```python
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool = False
)
...
```


```python

```

## 3. Request Body

- A request body is data sent by the client to your API.
- To declare a request body, you use Pydantic models.
- A request body is usually applicable to non-GET APIs (most POST)

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```


```python

```

## Request body + path + query parameters

- You can also declare body, path and query parameters, all at the same time

```python
@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

- If the parameter is also declared in the path, it will be used as a path parameter.
- If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter
- If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.


```python

```

## 4. Query Parameters and String Validations

- FastAPI allows you to declare additional information and validation for your parameters.

**Example 1.** Length of parameter doesn't exceed 50 characters and it is optional
```python
from fastapi import FastAPI, Query

@app.get("/items/")
def read_items(q: Optional[str] = Query(None, max_length=50)):
    ...
```
The `Optional` keyword is only to guide our code editor. Here, `None` is the default value.


**Example 2.** In addition, the minimum length should be 3
```python
@app.get("/items/")
def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    ...
```


**Example 3.** It should match the regex `^fixedquery$`
```python
@app.get("/items/")
def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    ...
```

**Example 4**. When you want to declare a variable as required while using `Query`
```python
@app.get("/items/")
def read_items(q: Optional[str] = Query(..., min_length=3)):
    ...
```
`...` is called the Ellipsis in Python.

**Example 5.** Query parameter list / multiple values
```python
@app.get("/items/")
def read_items(q: Optional[List[str]] = Query(None)):
    ...
```

**Example 6.** Query parameter list / multiple values with defaults
```python
@app.get("/items/")
def read_items(q: Optional[List[str]] = Query(["foo", "bar"])):
    ...
```

**Example 7.** Declare more metadata
```python
@app.get("/items/")
def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    ...
```
This indicates that the parameter
 - Is an alias for `item-query`
 - Has the mentioned title and decription
 - And is deprecated


```python

```

## 5. Path parameters and numeric validations



### Path parameters

- You can declare the same type of validations and metadata for path parameters with Path.
- You can declare all the same parameters as for `Query`.

For example,
```python
@app.get("/items/{item_id}")
def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    ...
```

### Numeric validations

- Just like string validations, you can also define numeric validations.
- Examples: `ge`: greater than or equal to, `le`: less than or equal to, `gt`: greater than, and `lt`: less than.

```python
@app.get("/items/{item_id}")
def read_items(
    item_id: int = Path(..., gt=0, lt=1)
):
    ...
```


```python

```

## 6. Multi-body parameters

- Like `Query` for query params and `Path` for path params, FastAPI has `Body` for body parameters.
- All the same arguments apply for body params
- As we saw earlier, FastAPI identifies body parameters if they are instances of `BaseModel`.

Example of defining path, query and body parameters together
```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
def update_item(
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    ...
```

### Specifying multiple body parameters

- Simply define multiple `BaseModel` derived classes

```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None
 ```
 
 - The expected body should look like this
 ```json
 {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

- Or the body parameters can be singular values
```python
def update_item(
    item_id: int, item: Item, user: User, importance: int = Body(..., title="", description="")
):
```

In this case, FastAPI will expect a body like:
```json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```


```python

```

## 7. Body - Fields

- You can declare validation and metadata inside of Pydantic models using Pydantic's `Field`.

- `Field` works the same way as Query, Path and Body, it has all the same parameters, etc.


```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
```


```python

```

## 8. Body - Nested Models

### How do we have arrays/ lists in body parameters?

- Use `List` datatype and include which type of objects should be entered in this.

Example:
```python
from typing import List, Optional, Set

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
```

### How do we have nested models?

- These Pydantic models act like `dict`s.

```python
class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None
```

- Or you can also have the nested model as a list:

```python
class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[List[Image]] = None
```


```python

```

## 9. Declare Request Example Data

- You can declare an example for a Pydantic model using `Config` and `schema_extra`.

```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
```

### Using `example`

- When using any of: `Path()`, `Query()`, `Header()`, `Cookie()`, `Body()`, `Form()`, `File()`
you can also declare a data example or a group of examples with additional information that will be added to OpenAPI.

```python
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    ...
````


```python

```

## 10. Extra data types
 List of additionl data types:
https://fastapi.tiangolo.com/tutorial/extra-data-types/


```python

```

## 11. Cookie parameters




```python


```
