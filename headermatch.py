from Bio import SeqIO

INFILE = "seqs.fas"
OUTFILE = "select_seqs.fas"

patterns = [
    "Eukaryota",
    "metagenome",
    "Homo Sapiens",
    "Mus musculus",
    "Rattus norvegicus",
    "Rhizobium",
    "Gorilla",
    "beringei",
    "thaliana",
    "Oryza sativa",
    "Dictyosteliu",
    "mitochondria",
    "Equus caballus",
    "Plasmodium falciparum",
    "Drosophila melanogaster",
]

for seq_record in SeqIO.parse(INFILE, "fasta"):
    for p in patterns:
        if p.lower() in seq_record.description.lower():
            with open(OUTFILE, "w") as outfile_handle:
                SeqIO.write(seq_record, outfile_handle, "fasta")
