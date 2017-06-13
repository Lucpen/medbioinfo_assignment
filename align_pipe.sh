#! /bin/bash -l

cd /home/lucia/applied_bioinfo/

module load bioinfo-tools
module load muscle

for fint in $( ls /home/lucia/applied_bioinfo/yeast_genes/);
do
muscle -in $fint -out "/home/lucia/applied_bioinfo/results/"$fint".afa"
done
