from Bio import SeqIO
import csv

def replace_headers_with_numeric_ids(input_file, output_fasta_file, output_csv_file):
    # Open the output files
    with open(output_fasta_file, 'w') as fasta_output, open(output_csv_file, 'w', newline='') as csv_output:
        # Prepare the CSV writer
        csv_writer = csv.writer(csv_output)
        # Write CSV header
        csv_writer.writerow(["Numeric_ID", "Original_Header"])

        # Read the input FASTA file
        for idx, record in enumerate(SeqIO.parse(input_file, "fasta"), start=1):
            # Create a unique numeric ID
            numeric_id = f"id_{idx}"
            # Write the mapping to the CSV file
            csv_writer.writerow([numeric_id, record.id])
            
            # Update the record's ID and description to numeric ID
            record.id = numeric_id
            record.description = ""
            # Write the modified record to the new FASTA file
            SeqIO.write(record, fasta_output, "fasta")

# Example usage
input_fasta_file = 'input.fasta'  # Change this to your input FASTA file path
output_fasta_file = 'output.fasta'  # The path for the modified FASTA file
output_csv_file = 'headers_mapping.csv'  # The path for the CSV file with mappings

replace_headers_with_numeric_ids(input_fasta_file, output_fasta_file, output_csv_file)