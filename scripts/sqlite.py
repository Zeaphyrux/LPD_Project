#!/usr/bin/python
import sys
import os 
import sqlite3
sys.path.insert(0, 'scripts')

PATH = 'output/'
DBNAME = 'LPD.db'
import settings
import RSA
import AES

DBNAME = PATH+DBNAME

global cursor
global conn

global dbname
global dbname_crypted
global key
from subprocess import Popen


def checkDb(db=DBNAME):
    '''check if db exists, if not it creates it'''
    #print dbname
    settings.init()
    #dbname = settings.getDatabase()
    #RSA.runDecrypt(dbname+'.crypt', keyFile=settings.getKeyPrivate())


    dbname_crypted  = db + '.crypt'


    dbExists = not os.path.exists(dbname_crypted)
    global cursor
    global conn
    global key
    global dbname
    dbname = db
    global dbname_crypted
    if dbExists:
        
        conn = sqlite3.connect(db)
        print "Database created"

    else:
        
        print "Database already exists"
        print "Decrypting...."
        key = settings.getKey()

        AES.decrypt_file(key, dbname_crypted, db, 16)
        print "Connecting....\n"
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        Popen(['rm', dbname_crypted])

        
'''
Simple function if we want to pass sql code directly
'''
def executeSQL(sqlCode):
    '''Run specified sqlCode'''
    global cursor
    cursor.execute(sqlCode)
    info = cursor.fetchall()
    for i in range(len(info)):
        print info [i]
    #print "Code runned"
'''
Creates table with given arguments
@table = table name  - string
@fields = fields name - MUST be an array
@types = format of the fields - MUST be an array
'''  
def createTable(table, fields,types):
    global cursor
    
    #Error check
    if len(fields) != len(types):
        print "The fields and types don't have the same number of elements, please correct them"
        return 0

    sql_base = """create table {0} (
    id          integer primary key autoincrement not null,
     """.format(table)
    sql_generate = ''
    for i in range(len(fields)):
        sql_generate += '{0}   {1}  ,'.format(fields[i], types[i])
    sql = sql_base + sql_generate
    sql= sql[:-1] + ')'
    #print sql
    cursor.execute(sql)
    print "Table {0} created".format(table)

'''
Drops table
@table = table name - string
'''
def dropTable(table):
    global cursor
    cursor.execute('DROP TABLE '+table)
    print "Table {0} dropped ".format(table)

'''
Inserts data into table
@conn = Database name
@table = table name    - string
@field = field name    - string
@value = value to set - string
The field and value can be several values, but must be the same number in each
'''
def insertIntoTable(table, field, value):
    global conn
    global cursor

    #formatting values to insert
    #value = value[1:-1].split(',')
    values = ''
    fields = ''

    for i in range(len(value)):
        if i==(len(value)-1):
            values+= "'"+value[i]+"'"
            fields+= field[i]
        else:
            values+= "'"+value[i]+"',"
            fields+= field[i]+","

    
    #print values
    sql = ''' INSERT INTO {0}({1})  VALUES({2}) '''.format(table, fields, values)
    #print sql
    #print sql
    cursor.execute(sql)
    conn.commit()
    print "Values inserted into {0}".format(table)

  
def showTables():
    """
    Query all tables in the database
    :param conn: the Connection object
    :return:
    """
    global cursor
    #cursor.execute('SELECT * FROM *')
    cursor.execute('''SELECT * FROM sqlite_master WHERE type='table' ''')

    tables = cursor.fetchall()
    print "Tables available are:"
    print tables[0]

'''
Selects field from table
@conn = Database name
@field = field name    - string
@table = table name    - string
@rows = number of rows - int
'''
def selectFromTable(table,field,  rowsNumber):
    global cursor
    cursor.execute('SELECT ' + field+' FROM '+ table)
    rows = cursor.fetchall()

    count=0
    if int(rowsNumber)==0:
        rowsNumber = 999999
    
    for row in rows:
        print row
        count+=1
        if count == rowsNumber:
            break
       
'''
Updates field with value in table where id is X
@table = table name - string
@field = field name - string
@value = value to update - string
@id = id number   - int
'''
def updateId(table, field, value, id):
    global cursor
    sql = '''UPDATE {0} SET {1} = '{2}' where id={3}'''.format(table,field, value, id)
   # print sql
    cursor.execute(sql)
    print "Id {0} updated in {1}".format(id, table)
def deleteId(table, id):
    sql = ''' DELETE FROM {0} WHERE id = {1}   '''.format(table, id)
    #print sql
    cursor.execute(sql)
    print "Id {0} deleted from {1}".format(id, table)
 

'''
Commits changes anc closes database
'''
def closeDb():
    global conn
    global key
    global dbname
    global dbname_crypted

    conn.commit()
    conn.close()
    print "Databased closed"
    print "Encrypting database...."
    AES.encrypt_file(key, dbname, dbname_crypted, 16)
    Popen(['rm', dbname])

    #settings.init()
    #RSA.runEncrypt(RSA_files[y], keyFile=settings.getKeyPublic())


#####################################
#                                   #
#      User interaction             #
#                                   #
#####################################

def userExecuteSql():
    sql = raw_input("Please provide the sql code to run on the database \n\n>>>  ")
    executeSQL(sql)
def userCreateTable():
    tableName = raw_input("Table name -->   ")
    fieldName =[]
    typeName = []
    count = 0
    print "Type quit to stop inserting data"
    print "Specifiy field name and data type ( text, int, real (float) or blob "
    while(True):
        
        fieldName.append(raw_input("Field {} --> ".format(count+1)))  
        if fieldName[count].lower()=="quit":
            fieldName.pop()
            break

        typeName.append(raw_input("Data type of {} --> ".format(fieldName[count])))
        count+=1
    createTable(tableName, fieldName, typeName)

def userDropTable():
    print "\t\tATTENTION  "
    print "This will delete the specified table including the data"
    print ""
    tableName = raw_input("Specifiy the table you wish to delete\n--> ")
    sure = raw_input("Are you sure you want to delete table {} ? (y/n)".format(tableName))
    if sure == 'y':
        dropTable(tableName)
    else:
        print "Exiting, table will not be deleted"
def userInsertTable():
    tableName = raw_input("Table name -->   ")
    fieldName = ''
    fieldName_bk = ''
    valueName = ''
    count = 0
    print "Type quit to stop inserting data"
    print "Specifiy field name and value to insert "
    while(True):
        
        fieldName = raw_input("Field --> ")  
        if fieldName.lower()=="quit":
            break
        if fieldName == '':
            fieldName = fieldName_bk
        valueName = raw_input("Value of {} --> ".format(fieldName))
        
        insertIntoTable(tableName, fieldName, valueName)
        fieldName_bk = fieldName
def userSelectTable():
    tableName = raw_input("Table name                -->  ")
    fieldName = raw_input("Field name    ( * for all)-->  ")
    rowNumber = raw_input("Number of rows( 0 for all)-->  ")
    selectFromTable(tableName, fieldName, rowNumber)

def userUpdateId():
    idd       = raw_input("Id to update           -->  ")
    tableName = raw_input("Table name to update   -->  ")
    fieldName = raw_input("Field name to update   -->  ")
    valueName = raw_input("Value to set         -->  ")
    updateId(tableName, fieldName, valueName, idd)
def userDeleteId():
    idd       = raw_input("Id to delete      --> ")
    tableName = raw_input("Table name        --> ")
    deleteId(tableName, idd)




def main():
    settings.init()
    a = settings.getDatabase()
    global key
    global dbname
    global dbname_crypted
    print a
    checkDb()

    #showTables(DBNAME)
    #insertIntoTable( 'sniff', 'dstmac, srcmac', 'AABBCCDDEE, DDEEFFCCAA')
    #selectFromTable( 'dstmac', 'sniff', 2)
    #insertIntoTable('sniff', 'dstmac, srcmac', 'AACCDD, DDEEAA')
    #a = ['teste', 'teste1', 'teste2']
    #b= ['text','text','text']
    #updateId('sniff', 'dstmac', 'EWQ', 1)
    #deleteId('sniff', 1)
    #dropTable('teste')
    #createTable('teste', a, b)
    #selectFromTable(DBNAME, 'sniff')

    closeDb()


if __name__=='__main__':
    main()
