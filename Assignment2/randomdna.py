#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Working in cd MANSSONLAB/Box\ Sync/Work/Conferences\ \&\ Courses/MedBioInfo/Code/
import random
# Asking for input
num = input("Length: ")
#Making sure it is a number
num = int(num)
# Choosing that number of random bases
base = ['A', 'T', 'G', 'C']
base2=base*num
random.shuffle(base2)
myrandomseq=base2[0:num]

# Writing on a file called randomf.fasta
f = open('randomf.fasta', 'w')
f.write('>myrandomsequence\n')  # python will convert \n to os.linesep
f.write(''.join(myrandomseq))
f.close()
