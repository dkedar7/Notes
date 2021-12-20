---
title: "Install Python 3 on Ubuntu"
author: "Kedar Dabhadkar"
date: 2021-02-22T05:46:18.464519
description: "Steps to install Python3.7 on an Ubuntu machine."
type: technical_note
draft: false
---
### Setup Python3.7 on Ubuntu
I often use a Google Cloud VM to for my projects. Depending on the type of the machine, it may or may not come with a preinstalled version of Python 3. Here's a simple snippet that I put together from multiple sources to install Python and configure pip on the environment.

```python
sudo apt update

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
sudo apt-get install python3.7-dev
sudo apt-get install python3.7-venv
sudo apt install python3-pip
```
