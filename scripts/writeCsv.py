#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Read and write functions for csv files'''
import csv


def writeCsv(data,filename):
    '''Gets list and filename, writes to csv format

    data:
        Array of data to write
    filename:
        File to write with column headers. If it already exists it appends
        and doesnt write the headers '''
    
    #sets filename with the correct extension
    if filename.endswith(".csv"):
       pass 
    else:
        filename+='.csv'

    f = open(filename, 'ab')
    
    writer = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    



    writer.writerow(data)


    #Wrap up
    f.close()
    

def readCsv(filename):
    '''Reads csv file row by row, returns list'''
    
    f = open(filename, 'rb')
    reader = csv.reader(f, delimiter=' ', quotechar='|')

    data = []
    for row in reader:
        data.append(row)

    return data



def main():
    test = [1,2,3,4,5,6]
    writeCsv(test, 'teste1.csv')
    #a = readCsv('teste.csv')
    #print a


if __name__=='__main__':
    main()
