---
title: "Q&A on Tabular Data with Huggingface"
author: "Kedar Dabhadkar"
date: 2021-06-05T05:46:18.464519
description: "How to get answers to natural language questions with Huggingface"
type: technical_note
draft: true
---
### Tabular Data Q&A

Learn how to ask natural language questions to your tabular data using Huggingface Transformers. The three most important dependencies are PyTorch, Transformers and PyTorch-scatter.

Current shortcoming: Doesn't wotk with non-string data


```python
# !pip install torch==1.8.0
# !pip install transformers
# !pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.8.0+cpu.html
```


```python
import pandas as pd
from transformers import pipeline
```

#### Import data


```python
data_df = pd.read_csv("https://raw.githubusercontent.com/dkedar7/Data-Analyzer/master/Analyzer/titanic.csv")
data_df = data_df.sample(100).reset_index(drop=True).astype(str)
```


```python
data_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>66</td>
      <td>1</td>
      <td>3</td>
      <td>Moubarek, Master. Gerios</td>
      <td>male</td>
      <td>nan</td>
      <td>1</td>
      <td>1</td>
      <td>2661</td>
      <td>15.2458</td>
      <td>nan</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>267</td>
      <td>0</td>
      <td>3</td>
      <td>Panula, Mr. Ernesti Arvid</td>
      <td>male</td>
      <td>16.0</td>
      <td>4</td>
      <td>1</td>
      <td>3101295</td>
      <td>39.6875</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>2</th>
      <td>209</td>
      <td>1</td>
      <td>3</td>
      <td>Carr, Miss. Helen "Ellen"</td>
      <td>female</td>
      <td>16.0</td>
      <td>0</td>
      <td>0</td>
      <td>367231</td>
      <td>7.75</td>
      <td>nan</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>3</th>
      <td>817</td>
      <td>0</td>
      <td>3</td>
      <td>Heininen, Miss. Wendla Maria</td>
      <td>female</td>
      <td>23.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101290</td>
      <td>7.925</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>489</td>
      <td>0</td>
      <td>3</td>
      <td>Somerton, Mr. Francis William</td>
      <td>male</td>
      <td>30.0</td>
      <td>0</td>
      <td>0</td>
      <td>A.5. 18509</td>
      <td>8.05</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>255</td>
      <td>0</td>
      <td>3</td>
      <td>Rosblom, Mrs. Viktor (Helena Wilhelmina)</td>
      <td>female</td>
      <td>41.0</td>
      <td>0</td>
      <td>2</td>
      <td>370129</td>
      <td>20.2125</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>96</th>
      <td>441</td>
      <td>1</td>
      <td>2</td>
      <td>Hart, Mrs. Benjamin (Esther Ada Bloomfield)</td>
      <td>female</td>
      <td>45.0</td>
      <td>1</td>
      <td>1</td>
      <td>F.C.C. 13529</td>
      <td>26.25</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>97</th>
      <td>798</td>
      <td>1</td>
      <td>3</td>
      <td>Osman, Mrs. Mara</td>
      <td>female</td>
      <td>31.0</td>
      <td>0</td>
      <td>0</td>
      <td>349244</td>
      <td>8.6833</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>98</th>
      <td>827</td>
      <td>0</td>
      <td>3</td>
      <td>Lam, Mr. Len</td>
      <td>male</td>
      <td>nan</td>
      <td>0</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>nan</td>
      <td>S</td>
    </tr>
    <tr>
      <th>99</th>
      <td>130</td>
      <td>0</td>
      <td>3</td>
      <td>Ekstrom, Mr. Johan</td>
      <td>male</td>
      <td>45.0</td>
      <td>0</td>
      <td>0</td>
      <td>347061</td>
      <td>6.975</td>
      <td>nan</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 12 columns</p>
</div>



#### Define transformers pipeline


```python
tqa = pipeline("table-question-answering", model="google/tapas-base-finetuned-wtq")
```


    Downloading:   0%|          | 0.00/1.63k [00:00<?, ?B/s]



    Downloading:   0%|          | 0.00/443M [00:00<?, ?B/s]



    Downloading:   0%|          | 0.00/262k [00:00<?, ?B/s]



    Downloading:   0%|          | 0.00/154 [00:00<?, ?B/s]



    Downloading:   0%|          | 0.00/490 [00:00<?, ?B/s]


#### Ask questions


```python
tqa(data_df, "Mean age")
```




    {'answer': 'AVERAGE > 16.0, 16.0, 71.0, 2.0',
     'coordinates': [(1, 5), (2, 5), (6, 5), (20, 5)],
     'cells': ['16.0', '16.0', '71.0', '2.0'],
     'aggregator': 'AVERAGE'}




```python
data_df.dtypes
```




    PassengerId      int64
    Survived         int64
    Pclass           int64
    Name            object
    Sex             object
    Age            float64
    SibSp            int64
    Parch            int64
    Ticket          object
    Fare           float64
    Cabin           object
    Embarked        object
    dtype: object




```python

```
