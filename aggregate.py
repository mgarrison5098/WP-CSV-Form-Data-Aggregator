import sys, getopt
import csv
from aggregators.form5 import form5Aggregator
from aggregators.formShared import formSharedAggregator
from aggregators.form1674 import form1674Aggregator


def main(argv):
    dataFile = './exports/single_export_raw.csv'
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
            elif row[0] == "1674":
                form1674Aggregator(row[1], row[2])
            else:
                if row[0].isdigit():
                    formSharedAggregator(row[0],row[1], row[2])
    

if __name__ == "__main__":
   main(sys.argv[1:])

# TO RUN:
# Make sure python is installed; cd into directory of aggregate.py; then run:
# python3 aggregate.py
# This will generate a separate CSV files in the /exports directory, one for each form ID