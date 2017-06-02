import csv


def func3():
    with open('secondFile.csv', 'r') as inp, open('final.csv', 'w') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        stuff = csv.reader(inp, delimiter=';')
        special = ''
        lines = [l for l in stuff]
        j = 0
        for line in lines:
            for i in line[4]:
                x = i.strip(':')  # remove all the ':' , '-' , 'T' in Time column, so It will be the Time of ID
                y = x.strip('-')
                z = y.strip('T')
                special += z
            lines[j][4] = special
            special = ''
            j += 1
        writer.writerows(lines)
