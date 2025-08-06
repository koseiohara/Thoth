import requests


def reference(doi):
    query = reference_query(doi)
    default(query, doi)
    query['author'] = getAuthors(query['author'])
    query['published'] = getDateTime(query['published'])
    #query['reference'] = getCitation(query['reference'])
    query['issue']  = query['issue']
    query['volume'] = query['volume']

    return query


def default(query, doi):
    query['author']    = query.setdefault('author'         , None)
    query['title']     = query.setdefault('title'          , None)
    query['publisher'] = query.setdefault('publisher'      , None)
    query['journal']   = query.setdefault('container-title', None)
    query['published'] = query.setdefault('published'      , None)
    query['issue']     = query.setdefault('issue'          , None)
    query['volume']    = query.setdefault('volume'         , None)
    query['page']      = query.setdefault('page'           , None)
    query['DOI']       = doi
    query['URL']       = query.setdefault('URL'            , None)

    #try:
    #    query['journal'] = query['content-domain']['short-container-title'][0]
    #    if (query['journal'] == []):
    #        raise ValueError
    #    print(query['journal'])
    #except:
    #    query['journal']   = query.setdefault('journal', None)

    if (query['journal'] is None or query['journal'] == []):
        query['journal'] = query['publisher']


def getAuthors(authors):
    if (authors == None):
        return None
    authors_num = len(authors)
    output = ['']*authors_num
    for i in range(authors_num):
        given  = authors[i]['given']
        family = authors[i]['family']
        
        output[i] = f'{family}, {given}'

    return output


def getDateTime(published):
    if (published == None):
        return None
    return published['date-parts'][0]
    #return [int(s) for s in published['date-parts'][0]]


def getCitation(cite):
    if (cite == None):
        return None
    cite_num = len(cite)
    output = ['']*cite_num
    for i in range(cite_num):
        print(cite[i])
        output[i] = cite[i]['unstructured']

    return output


def reference_query(doi):
    base_url = 'https://doi.org/'
    url = f'{base_url}{doi}'

    headers = {
        'Accept': "application/vnd.citationstyles.csl+json",
        'Yser-Agent': 'python-requests'
    }

    result = requests.get(url, headers=headers, timeout=10.)
    try:
        result.raise_for_status()
    except:
        raise ValueError(f'DOI {doi} does not exist')

    data = result.json()
    #if (data.get('status') != 'ok' or 'message' not in data):
    #    raise ValueError(f'Invalid response: {data}')

    return data


