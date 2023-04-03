from sys import argv
#python sys.argv[0] nodes.dmp query.fasta nt.m6 protista.m6 protista.fasta protista.krona.list
import os
from Bio import SeqIO
from taxid import taxid
from collections import defaultdict
taxid_1 = taxid(argv[1])

filter_taxid_list = ['33208','33090','2','4751','2157','81077','2731341','10239']
unknown_taxid_list = ['2787823','100272','61964','42452']

def nt_m6(nt_m6_file):
    protista_info,protista_taxid = {},{}
    m6_info = ''
    bitscore_query = defaultdict(float)
    with open(nt_m6_file) as fh:
        for line in fh.readlines():
            line = line.strip()
            query,*a,bitscore,staxid_2,stitle = line.split('\t')
            bitscore = float(bitscore)
            filter_subject = unkown_subject = False
            if bitscore < bitscore_query[query]:continue
            for i in filter_taxid_list:
                is_filter = taxid_1.is_sub(staxid_2,i)
                if is_filter == True:
                    m6_info += '#[Filted]#{}\n'.format(line)
                    filter_subject = True
                    break
                elif is_filter != False:
                    print(query,staxid_2,'taxid didnot found for parent id!',is_filter)
                    m6_info += '#[UnparentID]#{}\n'.format(line)
                    unkown_subject = True
                    break
            if filter_subject:
                break
            for i in unknown_taxid_list:
                is_unknown = taxid_1.is_sub(staxid_2,i)
                if is_unknown != False:
                    m6_info += '#[Unkown/ENV]#{}\n'.format(line)
                    unkown_subject = True
                    break
            if unkown_subject:
                continue
            else:
                m6_info += '{}\n'.format(line)
                protista_info[query] = m6_info
                protista_taxid[query] = staxid_2
                bitscore_query[query] = bitscore
    return protista_info,protista_taxid

protista_info,protista_taxid = nt_m6(argv[3])
if len(protista_info) > 0:
    fw_m6 = open(argv[4],'w')
    fw_krona = open(argv[6],'w')
    for query,info in protista_info.items():
        fw_m6.write(info)
        fw_krona.write('{}\t{}\n'.format(query,protista_taxid[query]))
    fw_m6.close()
    fw_krona.close()
    query_Protista_seq_records = []
    for seq_record in SeqIO.parse(argv[2], "fasta"):
        if seq_record.id in protista_info:
            query_Protista_seq_records.append(seq_record)
    SeqIO.write(query_Protista_seq_records,argv[5],'fasta')
