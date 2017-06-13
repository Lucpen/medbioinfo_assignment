#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Working in cd MANSSONLAB/Box\ Sync/Work/Conferences\ \&\ Courses/MedBioInfo/Code/
#"an_exon.fa"
file=input("Which file?")
seq=list()

with open(file,'r',encoding='utf-8') as the_file: #with will close it automatically
    for line in the_file:	#file is iterable
        if line.startswith(">") or line.startswith("#"):
            continue
        else:
            line=line.strip()
            seq.append(line)
    seq="".join(seq)
import utilsrna
tt = utilsrna.RNATranslationTable()

aa=list()
for i in range(0,(len(seq)-3),3):
    #print(i)
    aa.append(tt.translate(codon=seq[i:i+3]))

protlength=0
max_protlen=0
longest_prot=list()
prot=list()
for i in aa:
    if i!="*":
        prot.append(i)
        protlength=+1
    else:
        print("".join(prot))
        if protlength > max_protlen:
            longest_prot=prot
            max_protlen = protlength
        prot=list()
        protlength=0

print("\n")
print("The longest protein contains:",len(longest_prot),"amino-acids")
print("\n")
print("Its sequence is:")
print("".join(longest_prot))
print("\n")
