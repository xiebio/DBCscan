from sys import argv
import os
from collections import defaultdict
#python sys.argv[0] prosita.m6 animal.m6 in.fasta out.fasta
from Bio import SeqIO
query_score = defaultdict(float)
def parse_m6 (line):
    line = line.strip()
    query,*a,bitscore = line.split('\t')
    return query,bitscore

with open(argv[1]) as fh:
    for line in fh.readlines():
        query,bitscore = parse_m6(line)
        if float(bitscore) > query_score[query]:
            query_score[query] = float(bitscore)
with open(argv[2]) as fh:
    for line in fh.readlines():
        query,bitscore = parse_m6(line)
        if float(bitscore) > query_score[query]:
            del query_score[query]
if len(query_score) > 0:
    Protista_records = []
    for seq_record in SeqIO.parse(argv[3], "fasta"):
        if seq_record.id in query_score:
            Protista_records.append(seq_record)
    SeqIO.write(Protista_records,argv[4],'fasta')
