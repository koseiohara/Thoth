import re
from notion_client import Client

from getToken import getToken


def init(INDEX, FLAG):
    info = getToken(INDEX, FLAG)
    secret   = info[1]
    pagelink = info[2]

    if (pagelink[:22] != 'https://www.notion.so/'):
        raise ValueError('Invlid Notion Page Link. Reference may have already been initialized')

    #pageid = pagelink[22:54]
    pageid = extract_pageid(pagelink)

    databaseid = genDatabase(secret, pageid)

    updateCsv(INDEX, FLAG, secret, pageid, databaseid)


def extract_pageid(url):
    result = re.search(r'([0-9a-f]{32})', url)
    return result.group(1)


def genDatabase(secret, pageid):
    notion = Client(auth=secret)

    properties = {}
    properties = {
        'Title': {
            'title': {}
        },
        'First':{
            'multi_select': {}
        },
        'Category': {
            'multi_select': {}
        },
        'Authors': {
            'rich_text': {}
        },
        'Journal': {
            'multi_select': {}
        },
        'Year': {
            'number': {}
        },
        'Issue': {
            'number': {}
        },
        'Volume': {
            'number': {}
        },
        'Pages': {
            'rich_text': {}
        },
        'DOI': {
            'rich_text': {}
        },
        'URL': {
            'url': {}
        },
    }
    database = notion.databases.create(
        parent     = {'page_id': pageid},
        title      = [{'type': 'text', 'text': {'content': 'References'}}],
        properties = properties,
        is_inline  = True
    )

    return database['id']


def updateCsv(INDEX, FLAG, secret, pageid, databaseid):
    newLine = f'{FLAG},{secret},{pageid},{databaseid}\n'

    csv = open(INDEX, 'r+')
    output = ''
    for line in csv:
        result = line.split(',')
        if (result[0] == FLAG):
            output = output + newLine
        else:
            output = output + line

    csv.seek(0)
    csv.truncate()

    csv.write(output)
    csv.close()
    


