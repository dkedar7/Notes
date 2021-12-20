---
title: "Create Fake Data with Faker"
author: "Kedar Dabhadkar"
date: 2021-05-23T05:46:18.464519
description: "How to create fake data using the Python library, Faker"
type: technical_note
draft: false
---
### Create Fake Data with Faker

Having the ability to create dummy/ fake dataset is useful for a variety of reasons. Some use-cases that come to mind are 1. Testing python code, 2. Developing sample analysis, which can be replaced by real data later, 3. Writing tutorials, and 4. Proving a point. Yes, generating POCs, or Proof of Concepts, is a very important skill in data science, which helps to get stakeholder buy-in.


```python
# !pip install Faker
from faker import Faker
fake = Faker()
```

#### Some types of fake data


```python
# Fake name
fake.name()
```


```python
# Fake job
fake.job()
```


```python
# Fake color
fake.color_name()
```




    'YellowGreen'




```python
# Fake city
fake.city()
```




    'New Richardbury'




```python
# Fake text
fake.text()
```




    'Edge reflect under simple above. Security trial Democrat entire since something. Crime bag risk throw yard.\nSize sell hot have rise consider wife. Century play answer election clear ahead.'




```python
# Fake Boolean
fake.pybool()
```




    False




```python
# Fake list
fake.pylist(nb_elements=5, variable_nb_elements=False)
```




    ['http://williams-peterson.net/',
     Decimal('82966.369131538'),
     2841,
     'kathleen35@yahoo.com',
     'DiIHCibASmTFzRrDqZyQ']




```python
# Fake decimal
fake.pydecimal(left_digits=5, right_digits=6, positive=False, min_value=None, max_value=None)
```




    Decimal('42545.554972')




```python
## Some other providers:
fake.address()
fake.license_plate()
fake.swift()
fake.color()
fake.company()
fake.credit_card_full()
fake.currency()
fake.date_time()
fake.file_path()
fake.local_latlng()
fake.ascii_safe_email()
fake.job()
fake.paragraph(nb_sentences=5)
fake.fixed_width(data_columns=[(20, 'name'), (3, 'pyint', {'min_value':50, 'max_value':100})], align='right', num_rows=2)
fake.phone_number()
fake.profile()
fake.ssn()
fake.user_agent()
```




    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_1 like Mac OS X; szl-PL) AppleWebKit/532.39.2 (KHTML, like Gecko) Version/3.0.5 Mobile/8B113 Safari/6532.39.2'



#### Create fake data from a specific locale


```python
# Some locale options:
# 'it_IT','ja_JP', 'zh_CN', 'de_DE','en_US' and many more

fake = Faker('it_IT')
fake.address()
```




    'Rotonda Lisa 18\nPapetti salentino, 31326 Medio Campidano (PO)'



#### Create an entire profile at once


```python
fake = Faker()
fake.profile()
```




    {'job': 'Drilling engineer',
     'company': 'Trevino, Campbell and Young',
     'ssn': '608-83-8424',
     'residence': '321 Brian Valleys Suite 374\nWest Wendyville, CA 36613',
     'current_location': (Decimal('82.340949'), Decimal('-80.920579')),
     'blood_group': 'B-',
     'website': ['http://www.anderson-richardson.com/',
      'https://www.smith.net/',
      'http://fisher-romero.com/'],
     'username': 'gileslaura',
     'name': 'Ryan Miller',
     'sex': 'M',
     'address': '53066 Carr Centers\nWest Brianland, IA 06589',
     'mail': 'crystalgarrett@gmail.com',
     'birthdate': datetime.date(2012, 12, 8)}



### Read more

[1] https://faker.readthedocs.io/en/master/ <br>
[2] https://towardsdatascience.com/how-to-create-fake-data-with-faker-a835e5b7a9d9
