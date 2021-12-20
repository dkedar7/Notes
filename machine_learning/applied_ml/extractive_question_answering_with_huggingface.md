---
title: "Using Huggingface for Extractive Q&A"
author: "Kedar Dabhadkar"
date: 2021-06-06T05:46:18.464519
description: "How to use HuggingFace to build your own Q&A feature"
type: technical_note
draft: false
---
### Using Huggingface for Extractive Q&A

HuggingFace Transformers has many open-source, ready-to-use NLP models that we can simply plug into our use-case. For example, few months ago, I used their extractive Q&A models to build a webapp that answers questions from text data. You can check it out here: https://machinecomprehension-hpn4y2dvda-uc.a.run.app/. Here's how you can use some of their models for your own automated Q&A tasks.


```python
# !pip install transformers==4.6.1
# !pip install sentencepiece
# !pip install protobuf
```


```python
from transformers import pipeline
from transformers import AutoModelForQuestionAnswering
from transformers import AutoTokenizer
import pandas as pd
```

#### Write evaluation functions


```python
# Write a wrapper function to generate a Q&A pipeline from any specified model
def transformer_models(model_name):
    model =  AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return qa_pipeline


# Q&A using the default DistilBERT model
def distilbert_answer(context, query):
    '''
    Evaluate the specified context and query using DistilBERT
    '''
    distilbert_model = pipeline('question-answering')
    try:
        res = distilbert_model(question=query, context=context)
        return res['answer']
    except:
        return "Snap! The model couldn't find an answer. Try a different query."

    
# Q&A using the default RoBERTa model
def roberta_answer(context, query):
    '''
    Evaluate the specified context and query using RoBERTa
    '''
    roberta_model = transformer_models("deepset/roberta-base-squad2")
    try:
        res = roberta_model(question=query, context=context)
        return res['answer']
    except:
        return "Snap! The model couldn't find an answer. Try a different query."

    
# Q&A using the default ALBERT model
def albert_answer(context, query):
    '''
    Evaluate the specified context and query using ALBERT
    '''
    albert_model = transformer_models("twmkn9/albert-base-v2-squad2")
    try:
        res = albert_model(question=query, context=context)
        return res['answer']
    except:
        return "Snap! The model couldn't find an answer. Try a different query."
```

#### Input passage


```python
context = """Let me tell you how you can play the money beat on your drums. To get this beat going start 
with one part at a time. This way you can part your mind, and feel the groove a lot better. With your hi hat, 
play constant eight notes. We will add in some accents in the future, but for now, just play eight notes. 
Remember to count out loud when you are playing, it will help you out a lot!

Now that you have got this, try to not think about it. When people first learn to play the drums they usually 
think too much. This is where they start to make mistakes, they overthink. Your hi hat hand will not change 
this motion, so try to forget about it. Now it's time to concentrate on your other hand. With this hand, you will 
be playing quarter notes on the snare. These snare hits will be on the 2 and 4 count.

Good! Now let’s finish it off with the bass drum. This too will be playing quarter notes, however, not on the 
2 and four. Most beginners will have trouble with this, they will end up playing their snare and bass drum at 
the same time. Take your time and it will come to you. Play the bass on 1 and 3 counts."""
```


```python
context = context.replace("\n", " ")
```

#### Ask a question


```python
query = "What is this passage about?"
```


```python
# ALBERT
albert_answer(context, query)
```




    ' how you can play the money beat on your drums.'




```python
# DistilBERT
distilbert_answer(context, query)
```




    'where they start to make mistakes'




```python
# RoBERTa
roberta_answer(context, query)
```




    'money beat'



#### Let's compare answers for various questions


```python
queries = ["What is this passage about?",
          "How can one play the money beat?",
          "Where does on play the quarter notes?",
          "Where does one play the bass?",
          "What mistakes do beginners make?"]
```


```python
model_names = ["DistilBERT", "RoBERTa", "ALBERT"]
distilbert_answers, roberta_answers, albert_answers = [], [], []
for query in queries:
    distilbert_answers.append(distilbert_answer(context, query))
    roberta_answers.append(roberta_answer(context, query))
    albert_answers.append(albert_answer(context, query))
```


```python
results = pd.DataFrame()
results['Query'] = queries
results['DistilBERT'] = distilbert_answers
results['RoBERTa'] = roberta_answers
results['ALBERT'] = albert_answers
results
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
      <th>Query</th>
      <th>DistilBERT</th>
      <th>RoBERTa</th>
      <th>ALBERT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>What is this passage about?</td>
      <td>where they start to make mistakes</td>
      <td>money beat</td>
      <td>how you can play the money beat on your drums.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>How can one play the money beat?</td>
      <td>on your drums</td>
      <td>start  with one part at a time</td>
      <td>start  with one part at a time.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Where does on play the quarter notes?</td>
      <td>the snare</td>
      <td>on the snare</td>
      <td>on the snare.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Where does one play the bass?</td>
      <td>1 and 3 counts</td>
      <td>1 and 3 counts</td>
      <td>1 and 3 counts.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>What mistakes do beginners make?</td>
      <td>snare and bass drum</td>
      <td>they overthink</td>
      <td>playing their snare and bass drum at  the sam...</td>
    </tr>
  </tbody>
</table>
</div>



#### Read more

[1] HuggingFace Tranformers pipeline: https://huggingface.co/transformers/main_classes/pipelines.html#transformers.QuestionAnsweringPipeline <br>
[2] DiltilBERT: https://huggingface.co/transformers/model_doc/distilbert.html <br>
[3] RoBERTa: https://huggingface.co/transformers/model_doc/roberta.html <br>
[4] ALBERT: https://huggingface.co/transformers/model_doc/albert.html
