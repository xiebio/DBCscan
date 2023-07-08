# DBCscan：DNA Barcode based contamination scanner

Test script for protistan contamination screening

python DBCscan.py -i ./test_data/tpa_wgs.DWKX.1.fsa_nt.gz -o ./results

For testing purposes, all databases have just a few records. If you want to analyze real data, you should first download the full BOLD and nt&taxonomy database from boldsystems/NCBI. And split BOLD database into inclusion/exclusion sets using script ./lib/split_bold.py, then change the path in config file.

Any suggestions or problem, please contact Jiazheng Xie（xiejz@cqupt.edu.cn) .

Citation：
Xie, J.; Tan, B.; Zhang, Y. A Large-Scale Study into Protist-Animal Interactions Based on Public Genomic Data Using DNA Barcodes. Animals 2023, 13, 2243. https://doi.org/10.3390/ani13142243 
