

def doiFromFile(file):
    fp = open(file, 'r')
    result = []
    for doi in fp:
        work_doi = doi.strip('\n')
        work_doi = work_doi.strip()
        result.append(work_doi)

    return result

