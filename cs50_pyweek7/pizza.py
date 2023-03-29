from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) <2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a csv file!")
        else:
            print(table(sys.argv[1]))


def table(file):
    try:
        menu = []
        with open(file, "r") as f:
            reader = csv.reader(f)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File not found!")
                
if __name__ == "__main__":
    main()