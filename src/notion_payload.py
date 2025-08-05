from notion_client import Client


def duplication(notion, database_id, doi):
    next_query = None
    while True:
        # inquire 50 elements
        query = {
            'database_id': database_id,
            'filter': {
                'property': 'DOI',
                'rich_text': {
                    'equals': doi
                }
            },
            'page_size': 50,
        }
        if next_query:
            query['start_cursor'] = next_query

        result = notion.databases.query(**query)
        if (result.get('results', []) != []):
            print(f'DOI {doi} already exist')
            return True

        next_query = result.get('next_cursor')
        if not next_query:
            return False


def addPaper(notion, database_id, subpage_id, paper):

    payload ={}
    if (paper['title'] is not None):
        payload['Title'] = {
            'title': [
                #{
                #    'type': 'text',
                #    'text': {
                #            'content': paper['title']+' ',
                #            #'content': authors
                #    }
                #},
                {
                    'type': 'mention',
                    'mention': {
                        'type': 'page',
                        'page': {
                            'id': subpage_id
                        }
                    }
                }
            ]
        }

    if (paper['author'] is not None):
        # Lead Author Only
        payload['First'] = {
            'multi_select': [
                {
                    'name': paper['author'][0].replace(',', '')
                }
            ]
        }
        # All Authors
        authors = '; '.join(paper['author'])
        payload['Authors'] = {
            'rich_text': make_rich_text(authors)
        }

    if (paper['published'] is not None):
        payload['Year'] = {
            'number': int(paper['published'][0])
        }

    if (paper['publisher'] is not None):
        payload['Journal'] = {
            'multi_select': [
                {
                    'name': paper['publisher']                }
            ]
        }

    if (paper['issue'] is not None):
        payload['Issue'] = {
            'number': paper['issue']
        }

    if (paper['volume'] is not None):
        payload['Volume'] = {
            'number': paper['volume']
        }

    if (paper['page'] is not None):
        payload['Pages'] = {
            'rich_text': make_rich_text(paper['page'])
        }

    if (paper['DOI'] is not None):
        payload['DOI'] = {
            'rich_text': make_rich_text(paper['DOI'])
        }

    if (paper['URL'] is not None):
        payload['URL'] = {
            'url': paper['URL']
        }

    result = notion.pages.create(
        parent = {'database_id': database_id},
        properties = payload
    )

    print(' Successfully Imported : {}, DOI={}'.format(paper['title'], paper['DOI']))
    return result


def addChildPage(notion, page_id, paper):
    if (paper['title'] is not None):
        title = paper['title']
    else:
        title = 'Title Unknown: {}'.format(paper['doi'])


    # Generate a New Page
    child = notion.pages.create(
        parent = {'page_id': page_id},
        properties = {
            'title': {
                'title': [
                    {
                        'text': {
                            'content': title
                        }
                    }
                ]
            }
        }
    )
    new_page_id = child['id']

    #result = childPage_paragraph(notion, new_page_id, paper)
    result = childPage_database(notion, new_page_id, paper)

    return result, new_page_id


def childPage_database(notion, new_page_id, paper):
    if (paper['title'] is not None):
        title = paper['title']
    else:
        title = ''

    properties = {}
    properties = {
        'Title': {
            'title': {}
        },
        'Authors': {
            'rich_text': {}
        },
        'Journal': {
            'rich_text': {}
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
        parent     = {'page_id': new_page_id},
        title      = [{'type': 'text', 'text': {'content': 'Information'}}],
        properties = properties,
        is_inline  = True
    )

    database_id = database['id']

    payload = {}

    
    payload['Title'] = {
        'title': [
            {
                'type': 'text',
                'text': {
                    'content': title
                }
            }
        ]
    }

    if (paper['author'] is not None):
        payload['Authors'] = {
            'rich_text': make_rich_text('; '.join(paper['author']))
        }

    if (paper['published'] is not None):
        payload['Year'] = {
            'number': int(paper['published'][0])
        }

    if (paper['publisher'] is not None):
        payload['Journal'] = {
            'rich_text': make_rich_text(paper['publisher'])
        }

    if (paper['issue'] is not None):
        payload['Issue'] = {
            'number': int(paper['issue'])
        }

    if (paper['volume'] is not None):
        payload['Volume'] = {
            'number': int(paper['volume'])
        }

    if (paper['page'] is not None):
        payload['Pages'] = {
            'rich_text': make_rich_text(paper['page'])
        }

    if (paper['DOI'] is not None):
        payload['DOI'] = {
            'rich_text': make_rich_text(paper['DOI'])
        }

    if (paper['URL'] is not None):
        payload['URL'] = {
            'url': paper['URL']
        }

    result = notion.pages.create(
        parent = {'database_id': database_id},
        properties = payload
    )


def childPage_paragraph(notion, new_page_id, paper):
    # Make Contents
    info_list = []
    paragraph_append(info_list, 'Title', paper['title'])
    paragraph_append(info_list, 'Authors', '; '.join(paper['author']))
    paragraph_append(info_list, 'Journal', paper['publisher'])
    paragraph_append(info_list, 'Year', paper['published'][0])
    paragraph_append(info_list, 'Issue', paper['issue'])
    paragraph_append(info_list, 'Volume', paper['volume'])
    paragraph_append(info_list, 'Pages', paper['page'])
    paragraph_append(info_list, 'DOI', paper['DOI'])
    paragraph_append(info_list, 'URL', paper['URL'], paper['URL'])

    result = notion.blocks.children.append(block_id=new_page_id, children=info_list)

    return result


def paragraph_append(para, head, sentence, url=None):
    if (sentence is None):
        return

    para.append(
        {
            'object': 'block',
            'type': 'heading_3',
            'heading_3': {
                'rich_text': make_rich_text(head)
            }
        }
    )
    para.append(make_paragraph_text(str(sentence), url))


def make_rich_text(text, url=None):
    output = {
        'type': 'text',
        'text': {
            'content': text
        },
    }

    if (url is not None):
        output['text']['link'] = {'url': url}
    return [output]


def make_paragraph_text(text, url=None):
    output = {
        'object': 'block',
        'type': 'paragraph',
        'paragraph': {
            'rich_text': make_rich_text(text, url)
        }
    }
    return output


