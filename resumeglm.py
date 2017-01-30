import numpy as np

f1=open('ecogrid.glm','r')


lines=[]
for line in f1.readlines():
    lines.append(line.split())
    
lgf=len(lines)
print('lgf='+str(lgf)+'\n')
i=0
listNodes=[]
listMeter=[]
listlin=[]
listld=[]
while i<lgf-1:
     line=lines[i]
     
     
     if len(line)!=0:
         
         if (line[0]=="object"):
             if (line[1]=="node"):             
                 i+=2
                 line=lines[i]
                 listNodes.append(line[1])
             if (line[1]=="meter"):             
                 i+=1
                 line=lines[i]
                 listMeter.append(line[1])
             if (line[1]=="underground_line{"):
                 i+=2
                 name=lines[i][1]
                 i+=1
                 fr=lines[i][1]
                 i+=1
                 to=lines[i][1]
                 listlin.append([name, fr, to])
             if (line[1]=="load"):
                 i+=1
                 line=lines[i]
                 listld.append(line[1])
                 
     i+=1

#print(listlin)
lgnod=len(listNodes)
lgmeter=len(listMeter)
lglin=len(listlin)
lgld=len(listld)

with open('ecogrid_nod.txt','w') as fnod:
     fnod.writelines(["%s\n" % item  for item in listNodes])

with open('ecogrid_meter.txt','w') as fmeter:
     fmeter.writelines(["%s\n" % item  for item in listMeter])

with open('ecogrid_lin.txt','w') as flin:
     flin.writelines(["%s\n" % item  for item in listlin])
     
with open('ecogrid_ld.txt','w') as fld:
     fld.writelines(["%s\n" % item  for item in listld])
    
print(lgld)
print(lgmeter)
        #for j in range(0,3):
           
#            flin.write(str(listlin[i][0])+'   '+str(listlin[i][1])+'   '+str(listlin[i][2])+'\n')
#
#with open('ecogrid_nod2.txt','w') as fnod2:
#    fnod2.writelines(["%s\n" % item  for item in listNodes])
