# lssh - Lena SSH

Simple ssh profile management tool for the commandline.

## Install

* requires python 3.6 or higher
* requires ssh

Set your preferred editor with
``lssh config set editor nano``  
The default editor is sublime text 3

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