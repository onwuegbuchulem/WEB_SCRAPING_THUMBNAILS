import os

def rename_thumbnails(mapping_file, input_folder, output_folder):
    # Read the mapping file
    with open(mapping_file, 'r') as file:
        lines = file.readlines()

    # Check if 'Thumbnails Filenames' and 'Parent Filenames' headers are in the mapping file
    if 'Thumbnails Filenames' not in lines[0] or 'Parent Filenames' not in lines[0]:
        print("Invalid mapping file format. Headers not found.")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through rows in the mapping file (skipping the header)
    for line in lines[1:]:
        # Extract columns from the line
        columns = line.strip().split(' : ')

        # Check if the line has two columns
        if len(columns) == 2:
            thumbnail_filename, parent_filename = columns

            # Construct the full paths for input and output files
            input_path = os.path.join(input_folder, thumbnail_filename)
            output_path = os.path.join(output_folder, parent_filename.replace('.docx', '.jpg'))

            # Copy the file to the output folder with the new name
            os.rename(input_path, output_path)
            print(f'Renamed and moved: {thumbnail_filename} -> {parent_filename.replace(".docx", ".jpg")}')

# Example usage
mapping_file = 'mappingTableJPG/mapping.txt'
input_folder = 'Thumbnail256'
output_folder = 'MappedThumbnail256'
rename_thumbnails(mapping_file, input_folder, output_folder)
