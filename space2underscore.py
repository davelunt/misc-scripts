# Replaces space with underscore in fasta headers

from Bio import SeqIO

INFILE = "testncbi.fasta"
OUTFILE = "testncbi_underscores.fas"

with open(OUTFILE, "w") as outputs:
    for seqrecord in SeqIO.parse(INFILE, "fasta"):
        seqrecord.id = seqrecord.description.replace(" ", "_")
        seqrecord.description = seqrecord.id
        SeqIO.write(seqrecord, outputs, "fasta")
