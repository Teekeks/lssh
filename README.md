# lssh - Lena SSH

Simple ssh profile management tool for the commandline.

## Install

* requires python 3.6 or higher
* requires ssh and sshpass

Set your preferred editor with
``lssh config set editor nano``  
The default editor is nano

Copy content to a folder, cd into it and do the following:
```
chmod +x lssh.py
sudo ln -s /path/to/folder/lssh.py /usr/bin/lssh
sudo ln -s /path/to/folder/lssh-completion.bash /etc/bash_completion.d/lssh-completion.bash
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
or ``lssh c <name>``
* Set your preferred editor:
``lssh config set editor <editor command>``
* Change search path for Profiles:
``lssh config set profile_home <path>``
* Open the config:
``lssh config open``

## Configuration

| Option       | Type   | Default              |  Comment |
|--------------|--------|----------------------|---|
| editor       | String | nano                 |  The editor command used for opening configs and profiles |
| profile_home | String | {lssh_home}profiles/ |  The path to the location where lssh stores its profiles. |

## Profiles

| Option        | Type   | Default | Required? | Comment                                                                               |
|---------------|--------|---------|-----------|---------------------------------------------------------------------------------------|
| user          | String |         | Yes       | The username to log in with                                                           |
| ip            | String |         | Yes       | The IP of the remote Server                                                           |
| port          | Int    | 22      | Yes       | The Port of the remote Server                                                         |
| password      | String |         | No        | Password of remote user. Ignored if cert_file or password_file is set.                |
| cert_file     | String |         | No        | Path to certificate file to use for Login                                             |
| password_file | String |         | No        | Path to file containing the password of the remote user. Ignored if cert_file is set. |
| comment       | String |         | No        | A comment that will show up when ``lssh profile list`` is issued                      |