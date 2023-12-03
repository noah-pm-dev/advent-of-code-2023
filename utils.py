def readFile(day):
    with open(day + "/values.txt", 'r') as d:
        data = [data.rstrip() for data in d.readlines()]

    return data