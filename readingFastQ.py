#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Working in cd MANSSONLAB/Box\ Sync/Work/Conferences\ \&\ Courses/MedBioInfo/Code/
filename=input("File name: ")
line_IDs=[]
line_number=0

# Read the file
with open(filename,'r',encoding='utf-8') as file:
    for line in file:
        if line.startswith("@"):
            line_IDs.append(line)
            line_number+=1
        else:
            continue

print(line_number)

# To make it print an ID per line
for ID in line_IDs:
        print(ID)
