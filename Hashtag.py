import csv

import unicodecsv

list1 = []
with open('last_file.csv', 'r') as inp, open('hashtag.csv', 'w') as out:
    writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
    stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')
    c = "#"
    for row in stuff:
        for word in row[1].split(" "):
            if row[1][0] == c:
                if word not in list1:
                    list1 += [word]
                    writer.writerows(word)
