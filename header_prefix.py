# Prefix fasta header with text

from Bio import SeqIO

PREFIX = ""
INFILE = "testncbi.fas"
OUTFILE = "testncbi_prefixed.fas"

with open(OUTFILE, "w") as outputs:
    for seqrecord in SeqIO.parse(INFILE, "fasta"):
        seqrecord.id = PREFIX + seqrecord.description
        seqrecord.description = seqrecord.id
        SeqIO.write(seqrecord, outputs, "fasta")
