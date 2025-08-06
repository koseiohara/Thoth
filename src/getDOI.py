

def doiFromFile(file):
    fp = open(file, 'r')
    result = []
    for doi in fp:
        work_doi = doi.strip('\n')
        work_doi = work_doi.strip()
        if (work_doi != ''):
            work_doi = work_doi.split(',')
            result = result + [element for element in work_doi if element != '']
            #result.append(work_doi)

    return result


