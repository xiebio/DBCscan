from sys import argv
import sys
import os
#python sys.argv[0] in.m6 in.fasta out.fasta 
if not os.path.exists(argv[1]):
    sys.exit(0)
size = os.path.getsize(argv[1])
if size == 0:
    sys.exit(0)
from Bio import SeqIO
record_list = set()

with open(argv[1]) as m6_fh:
    for line in m6_fh.readlines():
        query = line.split('\t',1)[0]
        record_list.add(query)

seq_records = []
for record in SeqIO.parse(argv[2], "fasta"):
    if record.id in record_list :
        seq_records.append(record)

SeqIO.write(seq_records,argv[3],'fasta')
