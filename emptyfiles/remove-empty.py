# script to move empty fasta/fastq files to directory
# -------------------------------------------------------------
# this will not work on compressed .gz files
# entries should correspond to library and sample names

import os

# location of the data directories, must end in /
STARTDIR = "fasta_files"
EMPTYDIR = "empty_files"

# make a directory for empty files
os.makedirs(
    os.path.join(STARTDIR, EMPTYDIR), exist_ok=True
)  # succeeds even if directory exists


def is_empty_or_whitespace(file_path):
    if os.stat(file_path).st_size == 0:
        return True
    with open(file_path, "r") as file:
        content = file.read()
        if not content or content.isspace():
            return True
    return False


for root, dirs, files in os.walk(STARTDIR):
    for file in files:
        if file.endswith((".fasta", ".fastq")):  # specify file endings
            file_path = os.path.join(root, file)
            if is_empty_or_whitespace(file_path):
                new_path = os.path.join(EMPTYDIR, file)
                os.rename(file_path, new_path)
