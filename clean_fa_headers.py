# Replaces space, semicolon, colon, or parenthesis with underscore in fasta headers

from Bio import SeqIO

INFILE = "testncbi.fasta"
OUTFILE = "testncbi_underscores.fas"
EXCLUDED = [" ", ";", ":", "(", ")"]  # Characters to be replaced with underscores

# Read the input FASTA file and replace specified characters in headers
# Replace __ with _ in headers
# Write the modified sequences to the output file
with open(OUTFILE, "w") as outputs:
    for seqrecord in SeqIO.parse(INFILE, "fasta"):
        for char in EXCLUDED:
            seqrecord.id = seqrecord.id.replace(char, "_")
            seqrecord.description = seqrecord.description.replace(char, "_")
        # Ensure no double underscores remain in the headers
        seqrecord.id = seqrecord.id.replace("__", "_")
        seqrecord.description = seqrecord.description.replace("__", "_")
        SeqIO.write(seqrecord, outputs, "fasta")