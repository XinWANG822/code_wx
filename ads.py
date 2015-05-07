#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
f1= open(r"./sequence_GPCR.txt",'r')
f2= open(r"./out4.txt",'r')
fo= open(r"./Drug_sequence_GPCR.txt",'w+')
array=[]

lines=f1.readlines()
for j in range(len(lines)):
    temp =lines[j].strip()
    array.append(temp)
for s in f2:
    drug=[]
    s1=s.strip()
    s2=s1.split('\t')
    #print int(s2[0])
    if int(s2[0])!=-1:
        #drug=[]
        for k in range(len(s2)):
            if s2[k] in array:
               drug.append(int(s2[k]))
        if len(drug) == 0:
           drug.append(-1)
    else:
        drug.append(-1)
    for x in drug:
        fo.write(str(x) + '\t')
    fo.write( '\n')
    
    #print drug

    
    
        
        


    

