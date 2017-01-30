# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:10:31 2017

@author: mhurtgen
"""
import sqlite3

conn = sqlite3.connect('resumeglm')
cur=conn.cursor()


cur.execute('''
            SELECT COUNT(*) AS Nd FROM Nodes''')

n_nodes=cur.fetchone()[0]
print ('Number of nodes:'+str(n_nodes))

cur.execute('''
            SELECT COUNT(*) AS Ln FROM Lines''')

n_lines=cur.fetchone()[0]
print ('Number of lines:'+str(n_lines))

cur.execute('''
            SELECT COUNT(*) AS Ln FROM Loads''')

n_loads=cur.fetchone()[0]
print ('Number of loads:'+str(n_loads))


#cur.execute('''SELECT * FROM Nodes;''')
cur.execute('''SELECT Loads.Name, playerfile,Nodes.Name
                    FROM Loads JOIN Nodes
                    ON Loads.parent=Nodes.id''')
result=cur.fetchall()
print('get info:')
print(result)

cur.close()
conn.close()