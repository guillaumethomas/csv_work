import csv

BUGS = './bugs-2017-04-24.csv'


def read_bug_data(path):

    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row


def count_ite_per_keys(key, dicti, keys_lst, keys_count):

    #keys_lst = []
    #keys_count = []

    if dicti[key] not in keys_lst:
        keys_lst.append(row[key])
        keys_count.append([row[key], 1])
    else:
        keys_count[keys_lst.index(row[key])][1] += 1

    return keys_lst, keys_count


if __name__ == "__main__":
    users = []
    bugs_count = []
    c = []
    a = []
    for idx, row in enumerate(read_bug_data(BUGS)):


        if idx == 0:
            c = list(row.keys())
            for i in c:
                a.append([i, count_ite_per_keys(i, row, [],[] )])

        else:
            for i in row.keys():
                j = c.index(i)
                a[j][1] = count_ite_per_keys(i, row, a[j][1][0], a[j][1][1])


        if row['Assignee'] not in users:
            users.append(row['Assignee'])
            bugs_count.append([row['Assignee'],1])
        else:
            bugs_count[users.index(row['Assignee'])][1] += 1


        #print(row)
    for i in a:
        print(i[1][1])
    #print(a)
    #print(users)
    #print(bugs_count)