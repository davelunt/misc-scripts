# Convert alignment format with BioPython

from Bio import AlignIO

INPUT = "testseqs/ape.afa"
INFORMAT = "fasta"
OUTPUT = "testseqs/ape.phy"
OUTFORMAT = "phylip-relaxed"

with open(OUTPUT, "w") as outputs:
    ALIGNMENTS = AlignIO.parse(INPUT, INFORMAT)
    AlignIO.write(ALIGNMENTS, outputs, OUTFORMAT)

# could also use Bio.AlignIO.convert instead
# File Formats
# When specifying the file format, use lowercase strings. The same format names are also used in Bio.SeqIO and include the following:

# - clustal - Output from Clustal W or X, see also the module Bio.Clustalw which can be used to run the command line tool from Biopython.
# - emboss - EMBOSS tools’ “pairs” and “simple” alignment formats.
# - fasta - The generic sequence file format where each record starts with an identifer line starting with a “>” character, followed by lines of sequence.
# - fasta-m10 - For the pairswise alignments output by Bill Pearson’s FASTA tools when used with the -m 10 command line option for machine readable output.
# - ig - The IntelliGenetics file format, apparently the same as the MASE alignment format.
# - msf - The GCG MSF alignment format, originally from PileUp tool.
# - nexus - Output from NEXUS, see also the module Bio.Nexus which can also read any phylogenetic trees in these files.
# - phylip - Interlaced PHYLIP, as used by the PHLIP tools.
# - phylip-sequential - Sequential PHYLIP.
# - phylip-relaxed - PHYLIP like format allowing longer names.
# - stockholm - A richly annotated alignment file format used by PFAM.
# - mauve - Output from progressiveMauve/Mauve

# Note that while Bio.AlignIO can read all the above file formats, it cannot write to all of them.
