## Codon_Align
# Take unaligned fasta nucleotide file and fasta file of their
# amino acid translations and create a codon-aligned nucleotide fasta
# modified from https://github.com/santiagosnchez/CodonAlign.git


import sys
import warnings

warnings.simplefilter("ignore")

try:
    from Bio import AlignIO
    from Bio import SeqIO
    from Bio import codonalign
except ImportError:
    print(
        "Biopython (AlignIO, SeqIO) may not be installed. Try with: conda install biopython, or pip install biopython"
    )
    sys.exit()
else:
    # read data
    # alignment of amino acid sequences
    PRO_ALN = AlignIO.read("primates_protein_mafft.fas", format="fasta")
    # unaligned nucleotide seqs matching those in aa alignment
    NUC_SEQS = list(SeqIO.parse("primates.fas", format="fasta"))

    # set outfile for codon alignment
    CODON_OUTFILE = "primates_codons.fas"

    # get seq names from input files
    PRO_NAMES = [s.name for s in PRO_ALN]
    NUC_NAMES = [s.name for s in NUC_SEQS]

    # check that number of seqs match in aa and nucleotide files
    if len(PRO_NAMES) != len(NUC_NAMES):
        sys.exit("Number of sequences in both files does not match.")

    # check names match between nucleotide and amino acid files
    if all([name in PRO_NAMES for name in NUC_NAMES]) and all(
        [name in NUC_NAMES for name in PRO_NAMES]
    ):
        # build codon alignment
        try:
            CODON_ALN = codonalign.build(PRO_ALN, NUC_SEQS)
        except:
            print(
                "Could not generate codon alignment. Sequences probably include ambiguous or missing data.",
                file=sys.stderr,
            )
        else:
            # delete the <unknown description> label
            for i, _ in enumerate(CODON_ALN):
                CODON_ALN[i].description = ""
            # write to file
            AlignIO.write(CODON_ALN, CODON_OUTFILE, "fasta")
            print(
                f"{len(PRO_NAMES)} aligned CDS sequences saved to {CODON_OUTFILE}.",
                file=sys.stderr,
            )
    else:
        sys.exit("Amino acid and nucleotide sequences do not have the same labels.")
