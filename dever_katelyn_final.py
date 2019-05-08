# Katelyn Dever
# ITEC 2270 Final Project

import sqlite3
import random

# 7.1 generic superclass
class Employee:
    
    def __init__(self, idnumber, name):
        self.idnumber = idnumber
        self.name = name

# 7.2 senior subclass
class Manager(Employee):

    #7.2a constructor
    def __init__(self, idnumber, name, title):
        Employee.__init__(self, idnumber, name)
        # 7.2b data unique to this subclass
        self.title = title
        
    # 7.2c function giving command to junior subclass employee
    def giveCommand(self, Operator):
        print(self.name,"tells", Operator, "to work harder!")
        
# 7.3 junior subclass
class Operator(Employee):

    # 7.3a constructor
    def __init__(self, idnumber, name, status):
        Employee.__init__(self, idnumber, name)
        # 7.3b data unique to this subclass
        # (status = PTtemp, FTtemp, PTReg, FTReg)
        self.status = status

    # 7.3c receiving a command and carrying it out
    def receiveCommand(self, Manager):
        print(self.name, "hears the command from", Manager, "and decides to take a nap instead.")

# 7.5 method to create databases and insert values        
def createDatabase():
    conn = sqlite3.connect('employee.db')
    
    # create a table for managers
    conn.execute('''CREATE TABLE if not exists MANAGERS
                (IDNUMBER INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                TITLE TEXT);''')
    # create a table for operators
    conn.execute('''CREATE TABLE if not exists OPERATORS
                (IDNUMBER INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                STATUS TEXT);''')
    conn.close()

def getRandomID():
    return random.randint(1000,6000)

# 7.5 inserts records to MANAGERS table
def insertRecordM(value1, value2, value3):
    
    conn = sqlite3.connect('employee.db')
    
    # insert manager record
    conn.execute('''
                INSERT INTO MANAGERS(IDNUMBER, NAME, TITLE)
                VALUES(?,?,?)''', (value1, value2, value3))
    conn.commit()
    conn.close()

# 7.5 inserts records to OPERATORS table
def insertRecordO(value1, value2, value3):
    conn = sqlite3.connect('employee.db')
    
    # insert operator record
    conn.execute('''
                INSERT INTO OPERATORS(IDNUMBER, NAME, STATUS)
                VALUES(?,?,?)''', (value1, value2, value3))
    conn.commit()
    conn.close()

# 7.5 prints database contents
def printDatabase():
    conn = sqlite3.connect('employee.db')

    print("\nDatabase Contents:")
    print("Managers:")
    cursor = conn.execute("SELECT IDNUMBER, NAME, TITLE from MANAGERS")
    for row in cursor:
        tableid = row[0]
        name = row[1]
        title = row[2]
        print("ID:", tableid,"Name:",name,"Title:",title)

    print("Operators:")
    cursor = conn.execute("SELECT IDNUMBER, NAME, STATUS from OPERATORS")
    for row in cursor:
        tableid = row[0]
        name = row[1]
        status = row[2]
        print("ID:", tableid,"Name:",name,"Status:",status)

    # so it runs correctly each time
    conn.execute("DROP TABLE MANAGERS;")
    conn.execute("DROP TABLE OPERATORS;")
    

    conn.close()

#7.4 main function to demonstrate classes
def main():

    # 7.5 calls method to create database structure
    createDatabase()

    senior1ID = getRandomID()
    operator1ID = getRandomID()
    senior2ID = getRandomID()
    operator2ID = getRandomID()

    # 7.4 define objects, call interacting functions
    senior1 = Manager(senior1ID, 'Ariana Grande', 'Parts Distribution Manager')
    operator1 = Operator(operator1ID, 'Post Malone', 'RegFT')
    # 7.4 calls methods for giving and receiving commands
    senior1.giveCommand(operator1.name)
    operator1.receiveCommand(senior1.name)
    
    # creates table records for created objects
    insertRecordM(senior1.idnumber, senior1.name, senior1.title)
    insertRecordO(operator1.idnumber, operator1.name, operator1.status)

    # additional objects to demonstrate database
    senior2 = Manager(senior2ID, 'Demi Lovato', 'Sales Manager')
    insertRecordM(senior2.idnumber, senior2.name, senior2.title)
    operator2 = Operator(operator2ID, 'Donald Glover', 'TempPT')
    insertRecordO(operator2.idnumber, operator2.name, operator2.status)

    printDatabase()
    
    
main()
    
