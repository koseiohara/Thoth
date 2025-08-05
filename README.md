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
### Notion Setup
Before executing `thoth`, you need to set up Notion from [this page](https://www.notion.so/profile/integrations).
1. Click the `New Integration` button
1. Enter the settings for each field and push the `save` button
1. Copy the Internal Integration Secret and note it somewhere. You should check `Read content`, `Update content`, `Insert content`, and `No user information` in the Content Capabilities
After making these settings, open the Notion software and make a new private page.
1. Select `...` at the top right
1. Click `Connect to`. Then, click the connection you generated before
1. Click `Copy link` button in the same `...` and note it somewhere

### Python Setup<a id="PythonSetup"></a>
`thoth` needs `notion-client` and `requests`
```sh
$ pip install notion-client
$ pip install requests
```
Make `.notion_token.csv` at your home directory
```sh
$ touch ~/.notion_token.csv
```
Write the "referenceManager", internal integration secret, and Notion page link in the first line of `~/.notion_token.csv`
```csv
referenceManager,ntn_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,https://www.notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Usage
When `thoth` is used for the first time, initialize the Notion page
```sh
$ thoth init
```
This command will edit `~/.notion_token.csv` for future thoth execution.
Also, a database will be inserted to the Notion page.  

If you want to initialize `thoth` again, the `referenceManager` line in `~/.notion_token.csv` need to be deleted and rewritten exactly as in the [Python Setup](#PythonSetup).  

Now `thoth` is ready to manage articles.
You can add new bibliographic information from the command line
```sh
$ thoth add "doi_of_article"
```




