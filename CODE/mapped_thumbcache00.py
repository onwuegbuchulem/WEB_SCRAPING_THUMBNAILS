import os
import shutil

def rename_thumbnails(mapping_file, input_folder, output_folder):
    # Read the mapping file
    with open(mapping_file, 'r') as file:
        lines = file.readlines()

    # Check if 'Parent Docx File' and 'ThumbnailImage' headers are in the mapping file
    if 'Parent Docx File' not in lines[0] or 'ThumbnailImage' not in lines[0]:
        print("Invalid mapping file format. Headers not found.")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through rows in the mapping file (skipping the header)
    for line in lines[1:]:
        # Extract columns from the line
        columns = line.strip().split(',')

        # Check if the line has two columns
        if len(columns) == 2:
            parent_docx_file, thumbnail_image = columns

            # Construct the full paths for input and output files
            input_path = os.path.join(input_folder, thumbnail_image)
            output_path = os.path.join(output_folder, parent_docx_file)

            # Copy the file to the output folder with the new name
            shutil.copy2(input_path, output_path)
            print(f'Renamed and copied: {thumbnail_image} -> {parent_docx_file}')

# Example usage
mapping_file = 'mapping_table256/mapping.txt'
input_folder = 'THUMBNAILS256'
output_folder = 'MAPPED256'
rename_thumbnails(mapping_file, input_folder, output_folder)
