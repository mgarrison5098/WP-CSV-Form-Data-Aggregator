import sys, getopt
import csv
from aggregators.form5 import form5Aggregator


def main(argv):
    dataFile = './exports/single_export.csv'
    try:
        opts, args = getopt.getopt(argv,"hd")
    except getopt.GetoptError:
        print('aggregate.py -d <CSV/Data/File/Path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('aggregate.py -d <CSV/Data/File/Path>')
            sys.exit()
        elif opt in ("-d"):
            dataFile = arg

    with open(dataFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == "5":
                form5Aggregator(row[1], row[2])
            #else:
                
            #     runTest(row[1],row[3])
    

if __name__ == "__main__":
   main(sys.argv[1:])