import csv


def func2():
    with open('firstFile.csv', 'r') as inp, open('secondFile.csv', 'w') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        stuff = csv.reader(inp, delimiter=';')

        lines = [l for l in stuff]
        i = 0
        for row in lines:
            if row[0] == "HillaryClinton":  # If it is HillaryClinton, assign 'True' instead,
                lines[i][0] = "True"  # benenne sie um in "True"
            else:
                lines[i][0] = "False"  # If it is not assign 'False' instead"

            i = i + 1
        writer.writerows(lines)
