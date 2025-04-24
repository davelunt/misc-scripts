from pathlib import Path

def move_empty_or_whitespace_only_files(source_directory, target_directory):
    # Convert to Path objects
    source_path = Path(source_directory)
    target_path = Path(target_directory)

    # Create the target directory if it doesn't exist
    target_path.mkdir(parents=True, exist_ok=True)

    # Iterate over all files in the source directory and subdirectories
    for file_path in source_path.rglob('*'):
        if file_path.is_file():  # Check if it is a file
            # Check if the file is empty or contains only whitespace
            if file_path.read_text(encoding='utf-8').strip() == "":
                # Calculate the target file path
                target_file_path = target_path / file_path.name
                # Move the file to the target directory
                file_path.rename(target_file_path)
                print(f"Moved: {file_path} -> {target_file_path}")

# Specify the source directory and the target directory
source_directory = '/Users/bssdhl'  # Change this as needed
target_directory = '/Users/bssdhl/emptyfiles'

move_empty_or_whitespace_only_files(source_directory, target_directory)