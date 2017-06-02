import csv


def func1():
    with open('american-election-tweets.csv', 'r') as inp, open('firstFile.csv', 'w') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        stuff = csv.reader(inp, delimiter=';')

        all = []  # create new column
        row = next(stuff)
        row.append('hasHashtag')
        all.append(row)

        for row in stuff:
            if row[10] == "False":
                if "#" in row[1]:  # If Hashtag is used
                    row.append("True")  # Write 'True' to the column
                    writer.writerow(row)  # Write it to new .csv file called firstFile.csv
                else:
                    row.append("False")  # Write 'False' to the column
                    writer.writerow(row)  # Write it to new .csv file called firstFile.csv
                all.append(row)
        writer.writerows(all)
