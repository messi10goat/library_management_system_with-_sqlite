"""
Harsh Mittal
2018eeb1150@iitrpr.ac.in
"""

import sqlite3
import numpy as np

conn = sqlite3.connect('mydatabase1.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Book;


      
CREATE TABLE Student(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT NOT NULL  
);
CREATE TABLE Book(
    
    title TEXT NOT NULL,
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    student_id INTEGER
    
);                    
''')


def askname():
    n = input("Enter your name : ")
    return n

def asktitle():
    n=input("Enter the title : ")
    return n

def addstudent():
    n = askname()
    cur.execute(''' INSERT OR IGNORE INTO Student (name) VALUES (?) ''',(n,))
    
def addbook():
    n=asktitle()
    cur.execute('''INSERT OR IGNORE INTO Book (title,student_id) VALUES(?,?)''', (n,0))
    
def assignbook():
    n=askname()
    cur.execute('''SELECT count(*) FROM STUDENT where name = ?''',(n,))
    a=cur.fetchone()[0]
    if a==0:
        print("You are not registered. Please add yourself")
        addstudent();
        
    t=asktitle()
    cur.execute('''SELECT count(*) FROM Book where title = ?''',(t,))
    a=cur.fetchone()[0]
    if a==0:
        print("Book doesn't exist. Please retry")
        q = int(input("If you want to take anothe book, press 1. To exit, press 0"))
        if q==0:
            return
        else:
            assignbook()
        return
    cur.execute('''SELECT student_id FROM Book where title = ?''',(t,))
    a=cur.fetchone()[0]
    if a!=0:
        cur.execute('''SELECT name FROM Student WHERE id=?''',(a,))
        q = cur.fetchone[0]
        print("Book is already issued to ",q,".")
        q = int(input("To continue press 1. To exit press 0"))
        if q==0:
            return
        else:
            assignbook()
        return
    cur.execute('''SELECT id from Student where name = ?''',(n,))
    a = cur.fetchone()[0]
    cur.execute('''UPDATE Book SET student_id = ? WHERE name=?''',(a,t))
    print("Book is issued.")
    
def returnbook():
    n=askname()
    cur.execute('''SELECT count(*) FROM STUDENT where name = ?''',(n,))
    a=cur.fetchone()[0]
    if a==0:
        print("You are not registered. Please add yourself")
        addstudent();
    cur.execute('''SELECT id FROM Student WHERE name=?''',(n,))
    nid=cur.fetchone()[0]
        
    t=asktitle()
    cur.execute('''SELECT count(*) FROM Book where title = ?''',(t,))
    a=cur.fetchone()[0]
    if a==0:
        print("Book doesn't exist. Please retry")
        q = int(input("If you want to return anothe book, press 1. To exit, press 0"))
        if q==0:
            return
        else:
            returnbook()
        return
    cur.execute('''SELECT student_id FROM Book where title = ?''',(t,))
    a=cur.fetchone()[0]
    if a!=nid:
        print("You have not issued this book")
        return
    else:
        cur.execute('''UPDATE Book SET student_id=0 WHERE title=?''',(t,))
        
    
    
        
    
    
