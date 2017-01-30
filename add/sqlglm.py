# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:13:24 2017

@author: mhurtgen
"""
import sqlite3
import getinfo

f=open('ecogrid.glm','r')

i=iter(f)

conn = sqlite3.connect('resumeglm')
cur=conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Nodes;
    DROP TABLE IF EXISTS Linespacing;
    DROP TABLE IF EXISTS Lineconfig;
    DROP TABLE IF EXISTS Lines;
    DROP TABLE IF EXISTS Transformerconfig;
    DROP TABLE IF EXISTS Transformer;
    DROP TABLE IF EXISTS Lines_Nodes;
    DROP TABLE IF EXISTS Loads;
                
    CREATE TABLE Nodes (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         Name TEXT, 
         Voltage INTEGER, 
         Bustype TEXT
         );
    
    CREATE TABLE Transformerconfig (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT,
        Connection_type TEXT,
        Power INTEGER,
        Primary_voltage INTEGER,
        Secondary_voltage INTEGER
        );
    
    CREATE TABLE Transformer (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Configuration TEXT,
        Name TEXT,
        id_From INTEGER REFERENCES Nodes(id),
        id_To INTEGER REFERENCES Nodes(id)
        );
        
        
    CREATE TABLE Linespacing (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT           
    );
    
    CREATE TABLE Lineconfig (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT,
        id_spacing INTEGER REFERENCES Linespacing(id)  
    );
        
    CREATE TABLE Lines (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT,
        id_node1 INTEGER,
        id_node2 INTEGER,
        length INTEGER,
        id_config INTEGER REFERENCES Lineconfig(id)       
        );
        
    CREATE TABLE Loads (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT,
        parent INTEGER REFERENCES Nodes(id),
        playerfile TEXT,
        powerf FLOAT,
        currentpf FLOAT,
        impedancepf FLOAT,
        pfraction FLOAT,
        currentfraction FLOAT,
        impedancefraction FLOAT        
        );       
     ''')



for line in i:
    #print(line)
    if "node" in line:
        name,voltage=getinfo.readnode(i,line)
       
        cur.execute('''INSERT INTO Nodes (Name,Voltage)
                        VALUES (?,?)''',(name,voltage))
        conn.commit()
        
    if "meter" in line:
             

        
        name,voltage=getinfo.readmeter(i,line)
        
        cur.execute('''INSERT INTO Nodes (Name,Voltage)
                        VALUES (?,?)''',(name,voltage))
        conn.commit()
    
    if "object transformer_configuration" in line:
        name,conn_type,power,primary_v,secondary_v=getinfo.readtransformerconfig(i,line)
        
        cur.execute('''INSERT INTO Transformerconfig 
        (Name, Connection_type, Power, Primary_voltage, Secondary_voltage)
        VALUES (?,?,?,?,?)''', (name,conn_type,power,primary_v,secondary_v))
        conn.commit()        
    
    if "object transformer " in line:
        config,name,nd_from,nd_to=getinfo.readtransformer(i,line)
        
        cur.execute('SELECT id FROM Nodes WHERE name = ? ', (nd_from, ))
        From=cur.fetchone()[0]
        cur.execute('SELECT id FROM Nodes WHERE name = ? ', (nd_to, ))
        To=cur.fetchone()[0]        
        
        cur.execute('''INSERT INTO Transformer (Configuration, Name, id_From, id_To)
        VALUES(?,?,?,?)''', (config,name,From,To))
        conn.commit()        
        
    if "line_spacing" in line:
        linsp_name=next(i).split()
        name_sp=linsp_name[1].rstrip(';')
        cur.execute('''INSERT INTO Linespacing (Name)
                        VALUES (?)''',(name_sp, ))
        conn.commit()

    if "line_config" in line:

        name_cf,name_lspc=getinfo.readlinecf(i,line)        
        
        cur.execute('SELECT id FROM Linespacing WHERE name = ? ', (name_lspc, ))
        id_spacing = cur.fetchone()[0]
        
        cur.execute('''INSERT INTO Lineconfig (Name, id_spacing )
                        VALUES (?,?)''',(name_cf, id_spacing))
        conn.commit()
        
    if "object underground_line" in line:

        name,nd_from,nd_to,lg,name_config=getinfo.readundergrline(i,line)
        cur.execute('SELECT id FROM Lineconfig WHERE name = ? ', (name_config, ))
        id_config = cur.fetchone()[0]
        
        cur.execute('''INSERT INTO Lines (Name, id_node1, id_node2,  length, id_config)
                        VALUES (?,?,?,?,?)''',(name, nd_from, nd_to, lg, id_config))
        conn.commit()
    
    if "object load" in line:
        name, parent, playerfile, powerf, currentpf, impedancepf, pfraction,currentfraction,impedancefraction=getinfo.readload(i,line)        
        cur.execute('SELECT id FROM Nodes WHERE name = ? ', (parent, ))
        parentnode=cur.fetchone()[0]

        cur.execute('''INSERT INTO Loads (Name, parent, playerfile, 
        powerf, currentpf, impedancepf, pfraction, currentfraction, impedancefraction)
        VALUES (?,?,?,?,?,?,?,?,?)''', (name, parentnode, playerfile, powerf, currentpf, impedancepf, pfraction, currentfraction, impedancefraction))
               
        conn.commit()  
f.close()



cur.close()
conn.close()