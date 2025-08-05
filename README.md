# THOTH

A command line reference manager for Notion.
Source code is based on Python and Notion-API.

## Test Environment
macOS Sequoia 15.1  
Notion 4.16.2  
Python 3.9.6  
notion-client 2.4.0  
requests 2.32.4  

## Install and Build
Install the source code from GitHub
```sh
$ git clone https://github.com/koseiohara/Thoth.git
$ cd Thoth
$ make install
```
Source files will be copied to the directory specified by `INSTALL` in the `Makefile`.
Add the directory to the environment paths `PATH` and `PYTHONPATH`.  

When you uninstall this tool enter the command below:
```sh
$ make uninstall
```

## Setup
Before executing `thoth`, you need to set up Notion from <a id='https://www.notion.so/profile/integrations'>this page</a>

