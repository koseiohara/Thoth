from notion_client import Client

from getToken import getToken

file = './.token.csv'
flag = 'referenceManager'

def init():
    info = getToken(file, flag)
    secret   = info[1]
    pagelink = info[2]

    if (pagelink[:22] != 'https://www.notion.so/'):
        raise ValueError('Invlid Notion Page Link. Reference may have already been initialized')

    pageid = pagelink[22:54]

    databaseid = genDatabase(secret, pageid)

    updateCsv(flag, secret, pageid, databaseid)



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


def updateCsv(identifier, secret, pageid, databaseid):
    newLine = f'{identifier},{secret},{pageid},{databaseid}\n'

    csv = open(file, 'r+')
    output = ''
    for line in csv:
        result = line.split(',')
        if (result[0] == identifier):
            output = output + newLine
        else:
            output = output + line

    csv.seek(0)
    csv.truncate()

    csv.write(output)
    csv.close()
    


