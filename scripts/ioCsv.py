#!/usr/bin/python
import csv

PATH = "../output/csv/"
FILENAME = "teste.csv"



def writeCsv(data,filename=FILENAME, path=PATH):
    '''gets list and filename, writes to csv format'''
    
    #sets filename with the correct extension
    if filename.endswith(".csv"):
       pass 
    else:
        filename+='.csv'

    filename = path+filename
    f = open(filename, 'ab')
    
    writer = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(data)


    #Wrap up
    f.close()
    

def readCsv(filename, path=PATH):
    '''Reads csv file row by row, returns list'''
    
    filename = path+filename
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
