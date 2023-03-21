echo DWKX begin
python /lab/Parasites/github/DBCscan/lib/del2long.py /lab/Parasites/github/DBCscan/test_data/tpa_wgs.DWKX.1.fsa_nt.gz /lab/Parasites/github/DBCscan/results/0.assebly/DWKX 0
blastn -db /lab/Parasites/github/DBCscan/bold_test/BOLD_protista_test.fasta -query /lab/Parasites/github/DBCscan/results/0.assebly/DWKX -outfmt 6 -out /lab/Parasites/github/DBCscan/results/1.Protista_m6/DWKX.m6 -evalue 1e-5
python /lab/Parasites/github/DBCscan/lib/extract.py /lab/Parasites/github/DBCscan/results/1.Protista_m6/DWKX.m6 /lab/Parasites/github/DBCscan/results/0.assebly/DWKX /lab/Parasites/github/DBCscan/results/1.Protista_fas/DWKX
if [ -f "/lab/Parasites/github/DBCscan/results/1.Protista_fas/DWKX" ]; then
    blastn -db /lab/Parasites/github/DBCscan/bold_test/bold_non_protist_test.fasta -query /lab/Parasites/github/DBCscan/results/1.Protista_fas/DWKX -outfmt 6 -out /lab/Parasites/github/DBCscan/results/2.Non_Protista_m6/DWKX.m6 -evalue 1e-5
    python /lab/Parasites/github/DBCscan/lib/prosita_chop_animal.py /lab/Parasites/github/DBCscan/results/1.Protista_m6/DWKX.m6 /lab/Parasites/github/DBCscan/results/2.Non_Protista_m6/DWKX.m6 /lab/Parasites/github/DBCscan/results/1.Protista_fas/DWKX /lab/Parasites/github/DBCscan/results/2.Protista_choped_fas/DWKX
fi
if [ -f "/lab/Parasites/github/DBCscan/results/2.Protista_choped_fas/DWKX" ]; then
    blastn -outfmt '6 std staxid stitle' -query /lab/Parasites/github/DBCscan/results/2.Protista_choped_fas/DWKX -db /lab/Parasites/github/DBCscan/nt_test/nt_test.fasta -out /lab/Parasites/github/DBCscan/results/3.NT_m6/DWKX.m6 -evalue 1e-5
fi
echo DWKX done
