# lssh - Lena SSH

Simple ssh profile management tool for the commandline.

## Install

* requires python 3.6 or higher
* requires ssh

Set your preferred editor with
``lssh config set editor nano``  
The default editor is nano

Copy content to a folder, cd into it and do the following:
```
chmod +x lssh.py
sudo ln -s /usr/bin/lssh /path/to/folder/lssh.py
sudo cp ./lssh-completion.bash /etc/bash_completion.d/
```

## Usage

* Create a new profile:
``lssh profile create <name>``
* Open a profile:
``lssh profile show <name>``
* List all available profiles:
``lssh profile list``
* Connect to a profile:
``lssh connect <name>``
* Set your preferred editor:
``lssh config set editor <editor command>``