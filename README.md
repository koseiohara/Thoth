# THOTH

A command line reference manager for Notion.
Source code is based on Python and using the Notion-API.

## Test Environment
- macOS Sequoia 15.1
- Notion 4.16.2
- Python 3.9.6
    - notion-client 2.4.0
    - requests 2.32.4

## Install and Build
Install the source code from GitHub
```sh
$ git clone https://github.com/koseiohara/Thoth.git
$ cd Thoth
$ make install
```
The source files will be copied to the directory specified by `INSTALL` in the `Makefile`.
Add that directory to the environment paths `PATH` and `PYTHONPATH`.  

When you uninstall this tool, enter:
```sh
$ make uninstall
```

## Setup
### Notion Setup
Before running `thoth`, configure Notion integrations via [this page](https://www.notion.so/profile/integrations).
1. Click `New Integration`
1. Fill in the required fields and click `Save`.
1. Copy the Internal Integration Secret and note it somewhere. You should enable `Read content`, `Update content`, `Insert content`, and `No user information` in the Content Capabilities
Then, open the Notion and create a new private page.
1. Click `...` at the top right
1. Click `Connect to`, then choose the connection you generated before
1. Click `Copy link` button in the same `...` and note it somewhere

### Python Setup<a id="PythonSetup"></a>
`thoth` requires the `notion-client` and `requests` packages
```sh
$ pip install notion-client
$ pip install requests
```
Make `.notion_token.csv` in your home directory
```sh
$ touch ~/.notion_token.csv
```
Write the "referenceManager", internal integration secret, and Notion page link in `~/.notion_token.csv`
```csv
referenceManager,ntn_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,https://www.notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Usage
When using `thoth` for the first time, initialize the Notion page
```sh
$ thoth init
```
This command updates `~/.notion_token.csv` and inserts a database into the Notion page.  

To reinitialize `thoth`, delete and re-add the `referenceManager` line in `~/.notion_token.csv` as described in [Python Setup](#PythonSetup).  

Now `thoth` is ready to manage articles.
To add new bibliography entries from the command line
```sh
$ thoth add "doi_of_article1" "doi_of_article2" ...
```
Each time you add an article, a subpage is created in the page.
The `Title` column in each row of the database has a link to a subpage.
You can reorder and resize columns in the database as desired.

Strongly recommend adding the article's PDF file to every subpage by the `/pdf` Notion command.



