---
title: "Open Jupyter Lab on Google Cloud VM"
author: "Kedar Dabhadkar"
date: 2021-02-22T05:46:18.464519
description: "How to open a Jupyter Lab or Juyter Notebook on a Google Cloud Machine"
type: technical_note
draft: false
---
#### Step 1. Install Google Cloud 


```python
Follow the instructions to install Google Cloud SDK here: https://cloud.google.com/sdk/docs/install#mac
```

#### Step 2. Sign in into Google Cloud from the CLI and set a default project


```python
gcloud init
```

#### Step 3. Provision a VM from the Google Cloud Console


```python
https://console.cloud.google.com/home/dashboard
```

#### Step 4. Enter this command to connect to VM from the terminal


```python
gcloud compute ssh {instance-name} --ssh-flag="-L 8888:localhost:8888"
```

#### Step 5. Launch Jupyter Lab from the instance


```python
jupyter lab --port=8888
```
