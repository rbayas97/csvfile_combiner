import csv 
import sys
import os

def create_combined_csv(files):
    header_created = False
    for file in files:
        filename = os.path.basename(file)
        csvreader = csv.reader(open(file), delimiter = ",")        
        header = next(csvreader)
        if(header_created == False):
            header_created = create_header(header)
        create_rows(csvreader, filename)

def create_header(header):
    header.append('filename')
    print(','.join(header))
    return True

def create_rows(csvreader, filename):
    for row in csvreader:
        row.append(filename)
        print(','.join(row))

csv_files = sys.argv[1:]
create_combined_csv(csv_files)

