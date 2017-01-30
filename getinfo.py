# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 17:01:05 2017

@author: mhurtgen
"""

def readnode(i,line):
        next(i)#phase=next(i)        
        lin_name=next(i).split()
        name=lin_name[1].rstrip(';')
        
        next(i)
       # bustype=lin_bustype[1].rstrip(';')
        
        for k in range(0,3):
            next(i)

        lin_voltage=next(i).split()
        voltage=lin_voltage[1].rstrip(';')
        return name,voltage

def readmeter(i,line):
        #next(i)#phase=next(i)        
        lin_name=next(i).split()
        name=lin_name[1].rstrip(';')
        
        next(i)
       # bustype=lin_bustype[1].rstrip(';')
        
       
        lin_voltage=next(i).split()
        voltage=lin_voltage[1].rstrip(';')
        return name,voltage
 
def readtransformerconfig(i,line):
        lin_name=next(i).split()
        name=lin_name[1].rstrip(';')
        lin_connect=next(i).split()
        conn_type=lin_connect[1].rstrip(';')
        next(i)
        lin_power=next(i).split()
        power=lin_power[1].rstrip(';')
        lin_pv=next(i).split()
        primary_v=lin_pv[1].rstrip(';')
        lin_sv=next(i).split()
        secondary_v=lin_sv[1].rstrip(';')
        return name,conn_type,power,primary_v,secondary_v
       
def readtransformer(i,line):
        print(line)
        next(i);
        lin_config=next(i).split()
        print(lin_config)
        config=lin_config[1].rstrip(';')
        lin_name=next(i).split()
        name=lin_name[1].rstrip(';')
        lin_from=next(i).split()
        nd_from=lin_from[1].rstrip(';')
        lin_to=next(i).split()
        nd_to=lin_to[1].rstrip(';')
        return config,name,nd_from,nd_to
        
        
        
            
    
def readlinecf(i,line):
        lincf_name=next(i).split()
        name_cf=lincf_name[1].rstrip(';')
        
        lincf_spac=next(i).split()
        name_lspc=lincf_spac[1].rstrip(';')
        return name_cf, name_lspc
        
def readundergrline(i,line):
        next(i)        
        lin_name=next(i).split()
        name=lin_name[1].rstrip(';')
        
        lin_from=next(i).split()
        nd_from=lin_from[1].rstrip(';')
#        cur.execute('SELECT id FROM Nodes WHERE name = ? ', (nd_from, )) 
#        print(cur.fetchall())              
#        id_from = cur.fetchall()[0]
        
        lin_to=next(i).split()
        nd_to=lin_to[1].rstrip(';')
#        cur.execute('SELECT id FROM Nodes WHERE name = ? ', (nd_to, ))
#        id_to = cur.fetchall()[0][0]
        
        lin_length=next(i).split()
        #print(lin_length)
        lg=lin_length[1].rstrip(';')
        
        lin_config=next(i).split()
        name_config=lin_config[1].rstrip(';')
        return name,nd_from,nd_to,lg,name_config
        
def readload(i,line):
        lin_name=next(i).split()
        name=lin_name[1].rstrip(';')
        lin_parent=next(i).split()
        parent=lin_parent[1].rstrip(';')
        next(i)
        next(i)
        lin_playerfile=next(i).split()
        playerfile=lin_playerfile[1].rstrip(';')
        for k in range(0,16):
            next(i)
        lin_pf=next(i).split()
        powerf=lin_pf[1].rstrip(';')
        lin_currentpf=next(i).split()
        currentpf=lin_currentpf[1].rstrip(';')
        lin_impedancepf=next(i).split()
        impedancepf=lin_impedancepf[1].rstrip(';')
        
        lin_pfraction=next(i).split()
        pfraction=lin_pfraction[1].rstrip(';')
        lin_currentfraction=next(i).split()
        currentfraction=lin_currentfraction[1].rstrip(';')
        lin_impedancefraction=next(i).split()
        impedancefraction=lin_impedancefraction[1].rstrip(';')
        
        return name, parent, playerfile, powerf, currentpf, impedancepf, pfraction,currentfraction,impedancefraction
        
        
        
    
