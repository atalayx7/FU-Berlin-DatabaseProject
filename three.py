
import unicodecsv
def func3():
    with open('second_file.csv', 'r') as inp, open('third_file.csv', 'w') as out:
        writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
        stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')
        special = ''
        lines = [l for l in stuff]
        j=0
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
