from Bio import SeqIO

def clean_fasta_headers(input_file, output_file):
    # Characters to remove from headers
    chars_to_remove = ":,;()"

    # Read the input FASTA file
    records = SeqIO.parse(input_file, "fasta")

    # Process headers and write to a new FASTA file
    with open(output_file, 'w') as output_handle:
        for record in records:
            # Remove specified characters from the record id (header)
            record.id = ''.join(c for c in record.id if c not in chars_to_remove)
            # Remove specified characters from the description (if you want to clean it as well)
            record.description = ''.join(c for c in record.description if c not in chars_to_remove)
            SeqIO.write(record, output_handle, "fasta")

# Example usage
input_fasta_file = 'input.fasta'  # Change this to your input file
output_fasta_file = 'output_cleaned.fasta'  # The cleaned output file

clean_fasta_headers(input_fasta_file, output_fasta_file)