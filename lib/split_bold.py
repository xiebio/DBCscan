from sys import argv
#python sys.argv[0] BOLD_DB_PATH OUTDIR 
from Bio import SeqIO
import re
Protista_records = []
Non_Protista_records = []
for seq_record in SeqIO.parse(argv[1], "fasta"):
    if matchobj := re.match(r'.*\|Protista,([^,]*)',seq_record.description):
        Protista_records.append(seq_record)
    else:Non_Protista_records.append(seq_record)
SeqIO.write(Protista_records,argv[2]+'/BOLD.Protista.fasta','fasta')
SeqIO.write(Non_Protista_records,argv[2]+'/BOLD.Non_Protista.fasta','fasta')
