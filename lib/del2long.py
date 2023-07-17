from sys import argv
#python sys.argv[0] in.fasta out.fasta chop 
#delete contigs longer than 10000
from Bio import SeqIO
import gzip

seq_records = []
f = gzip.open(argv[1], 'rt')
for record in SeqIO.parse(f, "fasta"):
    if len(argv)>3 and len(record.seq)>100000:continue
    seq_records.append(record)

f.close()
SeqIO.write(seq_records, argv[2], "fasta")
