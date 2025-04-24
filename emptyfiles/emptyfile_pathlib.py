from pathlib import Path

def find_empty_or_whitespace_only_files(directory):
    empty_or_whitespace_files = []

    # Create a Path object for the directory
    directory_path = Path(directory)

    # Iterate over all files in the directory and subdirectories
    for file_path in directory_path.rglob('*'):  # Use rglob to search recursively
        if file_path.is_file():  # Ensure it's a file
            # Read the file and check if it's empty or contains only whitespace
            if file_path.read_text(encoding='utf-8').strip() == "":
                empty_or_whitespace_files.append(str(file_path))

    return empty_or_whitespace_files

# Specify the directory you want to search
directory_to_search = '/Users/bssdhl'  # Change this as needed

result = find_empty_or_whitespace_only_files(directory_to_search)
print("Empty or whitespace-only files:")
for file_path in result:
    print(file_path)