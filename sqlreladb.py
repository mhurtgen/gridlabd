# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:01:12 2017

@author: mhurtgen
"""
import sqlite3
import getinfo
#Fill junction table li
f=open('ecogrid.glm','r')

i=iter(f)

conn = sqlite3.connect('resumeglm')
cur=conn.cursor()

cur.executescript('''
 DROP TABLE IF EXISTS Lines_Nodes;

 CREATE TABLE Lines_Nodes (
        line_id INTEGER REFERENCES Lines(id),
        node_id INTEGER REFERENCES Nodes(id),
        PRIMARY KEY(line_id,node_id)        
        );        
     ''')

for line in i:
    if "object underground_line" in line:

        name,nd_from,nd_to,lg,name_config=getinfo.readundergrline(i,line)

        cur.execute('SELECT * FROM Lines WHERE Name=?',(name, ))
        id_line = cur.fetchone()[0]        
        
        cur.execute('SELECT * FROM Nodes WHERE Name=?',(nd_from, ))
        id_from = cur.fetchone()[0]
        cur.execute('''INSERT INTO Lines_Nodes (line_id, node_id)
        VALUES (?,?)''',(id_line,id_from))

        cur.execute('SELECT * FROM Nodes WHERE Name=?',(nd_to, ))
        id_to = cur.fetchone()[0]
        cur.execute('''INSERT INTO Lines_Nodes (line_id, node_id)
        VALUES (?,?)''',(id_line,id_to))
        
        conn.commit()
        
f.close()



cur.close()
conn.close()

