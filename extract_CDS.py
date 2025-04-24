# Extract CDS feature(s) translations from genbank file and save to fasta

from Bio import SeqIO

# Define input and output file paths
INFILE = "testseqs/Bplicatilis-mtgenome.gb"
OUTFILE = "Bp_cds.fas"

# Open the output file in write mode
with open(OUTFILE, "w") as output_handle:
    # Iterate over each record in the input GenBank file
    for seq_record in SeqIO.parse(INFILE, "genbank"):
        # Iterate over each feature in the current GenBank record
        for seq_feature in seq_record.features:
            # If the feature is a Coding Sequence (CDS)
            if seq_feature.type == "CDS":
                output_handle.write(
                    # save translation of feature from gb record to fasta file
                    # f">{seq_feature.qualifiers['product'][0]}\n{seq_feature.qualifiers['translation'][0]}\n"
                    # extract the feature's sequence to fasta, NB not just exons, this includes introns
                    f">{seq_feature.qualifiers['product'][0]}\n{seq_feature.location.extract(seq_record).seq}\n"
                )
