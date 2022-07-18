import csv
import sys

# returns a nested list of contents
def read_csv_from_file(filename):
    contents = []
    path = filename

    with open(path, 'r', newline='', encoding='latin-1') as Housing:
        my_reader = csv.reader(Housing, delimiter=',', quotechar='|')

        segment = []
        next(my_reader)
        for i, row in enumerate(my_reader):
            segment = []
            contents.append(row)

        return contents

if __name__ == "__main__":
    if len(sys.argv) == 2:
        contents = read_csv_from_file(sys.argv[1])
    else:
        print("Needs a spreadhsheet file")

