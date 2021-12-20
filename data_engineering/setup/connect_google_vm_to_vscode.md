---
title: "Connect Google VM to VS Code"
author: "Kedar Dabhadkar"
date: 2021-05-30T05:46:18.464519
description: "How to connect a Google Vm to VS Code"
type: technical_note
draft: false
---
### Connect Google VM to VS Code

I do most of my development on a Google Cloud VM and I am a big fan of VS Code. For a long time, when programming on GCP, I only used the Jupyter IDE. After looking for a while, I was able to connet a GCP VM to VS Code. Here's how:

#### Step 1. Create an SSH key locally
ssh-keygen -t rsa -f ~/.ssh/[KEY_FILENAME] -C [USERNAME]
[KEY_FILENAME] is any name that you want to give to your key and [USERNAME] is usually the first half of your email address (username@gmail.com).

This generates a private and a public key on the VM.

Don't forget to change the permissions on your key:


```python
chmod 400 ~/.ssh/[KEY_FILENAME]
```

#### Step 2. Add the key to GCP VM

Go to the GCP instance -> "SSH Keys" -> click "Show and edit". 

Copy contents of the public ssh key [KEY_FILENAME].pub and paste it on the GCP console window.

#### Step 3. Install the SSH plugin on VS Code

Install this plugin on VS Code: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit

#### Step 4. Add SSH Host to VS Code

Bring up the command palette on VS Code using "Cmd+Shift+p". Select "Remote - SSH: Add New SSH Host"

Enter the following SSH command and add it to the default config file


```python
ssh -i ~/.ssh/[KEY_FILENAME] [USERNAME]@[External IP]
```

#### Step 5. Connect to the VM!

Select the remote explorer plugin icon from the left and connect to the VM!

#### Read more

https://towardsdatascience.com/unleash-the-power-of-visual-studio-code-vscode-on-google-cloud-platform-virtual-machine-f75f78f49aee
