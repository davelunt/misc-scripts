# Biopython's SeqIO module handles sequence input/output
# https://widdowquinn.github.io/2018-03-06-ibioic/01-introduction/03-parsing.html

from Bio import SeqIO

def get_cds_feature_with_qualifier_value(seq_record, name, value):
    """Function to look for CDS feature by annotation value in sequence record.
    
    e.g. You can use this for finding features by locus tag, gene ID, or protein ID.
    """
    # Loop over the features
    for feature in genome_record.features:
        if feature.type == "CDS" and value in feature.qualifiers.get(name, []):
            return feature
    # Could not find it
    return None

genome_record = SeqIO.read("NC_004547.gbk", "genbank")
cds_feature = get_cds_feature_with_qualifier_value(genome_record, "old_locus_tag", "ECA0662")
print(cds_feature)


