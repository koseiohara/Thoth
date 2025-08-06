
def getToken(file, flag):
    csv = open(file, 'r')
    result_flag = ''
    for line in csv:
        result = line.strip('\n')
        result = result.split(',')
        if (result[0] == flag):
            csv.close()
            return result

    csv.close()
    return None



