import sys
f1= open(r"./DT_commn_sequence.txt",'r')
f2= open(r"./D_T_Relation_Inner_sequence.txt",'r')
fo= open(r"./DT_Relation_Inner_sequence.txt",'w+')
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
