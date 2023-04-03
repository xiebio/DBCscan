import getopt
import sys
import os
def parse_config (config_file):
    parameters_dict = {
            'protista_db':'',
            'non_protista_db':'',
            'nt_db':'',
            'nt_taxonomy':'',
            'krona_path':'',
            }
    with open (config_file) as fh:
        for line in fh.readlines():
            line = line.strip()
            name,path = line.split('=')
            if name in parameters_dict:
                if os.path.isabs(path):
                    parameters_dict[name] = path
                else:
                    parameters_dict[name] = os.path.join(config_dir,path)
    return parameters_dict

def usage():
    '''
    help
    '''
    print("Usage: DBCscan.py -h help -a config_file -i input_assembly -o out_dir -c")
    print("-c if defined, the contigs longer than 100000 will be discarded at first")
    print("-o --out_dir outdir[default:./]")

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:i:o:c",
                ["help", "config_file=", "input_assembly=","out_dir=", "chop"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    program_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
    config_file = program_dir+'/DBCscan.config'
    outdir = './'
    assembly = ''
    chop = 0
for o, a in opts:
    if o in ('-h', '--help'):
        usage()
        sys.exit()
    elif o in ("-a", "--config_file"):
        config_file = os.path.abspath(a)
    elif o in ("-i", "--input_assembly"):
        assembly = os.path.abspath(a)
    elif o in ("-o", "--out_dir"):
        outdir = os.path.abspath(a)
    elif o in ("-c", "--chop"):
        chop = 1
if not assembly:
    print('-i/--input_assembly must be set!')
    usage()
    sys.exit(2)

config_dir = os.path.dirname(config_file)
parameters_dict = parse_config(config_file)
outdir_list = [
    outdir,
    outdir+'/0.assebly',
    outdir+'/1.Protista_fas',
    outdir+'/1.Protista_m6',
    outdir+'/2.Non_Protista_m6',
    outdir+'/2.Protista_choped_fas',
    outdir+'/3.NT_m6',
    outdir+'/4.Protist_fas',
    outdir+'/4.Protista_m6',
    outdir+'/5.Krona'
        ]
for i in outdir_list:
    if not os.path.exists(i):os.mkdir(i)
prefix = os.path.basename(assembly)
prefix = prefix.split('.')[1]
with open(outdir+'/run_DBCscan.sh','w') as fh:
    fh.write(
'''echo {1} begin
python {6}/lib/del2long.py {2} {0}/0.assebly/{1} {5}
blastn -db {3} -query {0}/0.assebly/{1} -outfmt 6 -out {0}/1.Protista_m6/{1}.m6 -evalue 1e-5
python {6}/lib/extract.py {0}/1.Protista_m6/{1}.m6 {0}/0.assebly/{1} {0}/1.Protista_fas/{1}
if [ -f "{0}/1.Protista_fas/{1}" ]; then
    blastn -db {4} -query {0}/1.Protista_fas/{1} -outfmt 6 -out {0}/2.Non_Protista_m6/{1}.m6 -evalue 1e-5
    python {6}/lib/prosita_chop_animal.py {0}/1.Protista_m6/{1}.m6 {0}/2.Non_Protista_m6/{1}.m6 {0}/1.Protista_fas/{1} {0}/2.Protista_choped_fas/{1}
fi
if [ -f "{0}/2.Protista_choped_fas/{1}" ]; then
    blastn -outfmt '6 std staxid stitle' -query {0}/2.Protista_choped_fas/{1} -db {7} -out {0}/3.NT_m6/{1}.m6 -evalue 1e-5
    python {6}/lib/nt_m6_extract.py {8} {0}/2.Protista_choped_fas/{1} {0}/3.NT_m6/{1}.m6 {0}/4.Protista_m6/{1}.m6 {0}/4.Protist_fas/{1} {0}/5.Krona/{1} 
fi
if [ -f "{0}/5.Krona/{1}" ]; then
    ktImportTaxonomy -o {0}/5.Krona/{1}.html {0}/5.Krona/{1}
fi
echo {1} done
'''.format(outdir, prefix, assembly, parameters_dict['protista_db'], parameters_dict['non_protista_db'], chop, program_dir, parameters_dict['nt_db'], parameters_dict['nt_taxonomy'] ))
os.system("sh {}/run_DBCscan.sh".format(outdir))
